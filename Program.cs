using System;
using System.Xml.Linq;
using System.Linq;
using System.Collections.Generic;
using System.Drawing;

class Program
{
    static void Main(string[] args)
    {
        string filePath = @"X:\Scripts\TEST\EplanMacroInterpreter\funcionamiento_macros\Lineas.ema";
        string outputPath = @"X:\Scripts\TEST\EplanMacroInterpreter\funcionamiento_macros\Lineas3.png";
        
        XDocument doc = XDocument.Load(filePath);
        var objects = ParseEplanObjects(doc);
        DrawObjects(objects, outputPath);
    
    }

    static List<EplanObject> ParseEplanObjects(XDocument doc)
    {
        var objects = new List<EplanObject>();

        foreach (var element in doc.Descendants().Where(e => e.Name.LocalName.StartsWith("O")))
        {
            var type = element.Name.LocalName;
            switch (type)
            {
                case "O31": // Línea
                    objects.Add(new EplanLine(element));
                    break;               
                default:
                    Console.WriteLine($"Tipo de objeto no manejado: {type}");
                    break;
            }
        }

        return objects;
    }

    static void DrawObjects(List<EplanObject> objects, string outputPath)
    {
        int width = 2000, height = 2000;
        using (Bitmap bmp = new Bitmap(width, height))
        using (Graphics g = Graphics.FromImage(bmp))
        {
            g.Clear(Color.White);
            g.TranslateTransform(width / 2, height / 2);
            g.ScaleTransform(1, -1); // Invertir axis Y so it can work with the coords of eplan 

            foreach (var obj in objects)
            {
                obj.Draw(g);
            }

            bmp.Save(outputPath);
        }
    }
}

abstract class EplanObject
{
    public abstract void Draw(Graphics g);

    protected static PointF ParsePoint(string coord)
    {
        var parts = coord.Split('/');
        return new PointF(float.Parse(parts[0]), float.Parse(parts[1]));
    }
}

class EplanLine : EplanObject
{
    public PointF Start { get; }
    public PointF End { get; }

    public EplanLine(XElement element)
    {
        Start = ParsePoint(element.Attribute("A531")?.Value);
        End = ParsePoint(element.Attribute("A532")?.Value);
    }

    public override void Draw(Graphics g)
    {
        g.DrawLine(Pens.Black, Start, End);
    }
}

