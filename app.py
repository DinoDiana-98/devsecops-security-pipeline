"""
DevSecOps Demo Application
Una aplicación web simple para demostrar un pipeline de seguridad automatizado.
Autor: Leidy Diana Principe Quispe
Proyecto: Portafolio de Ciberseguridad 2026
"""
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Página principal 
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevSecOps Demo | Leidy Principe</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0f1c 0%, #1a1a2e 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .card {
            background: rgba(26, 26, 46, 0.95);
            border-radius: 20px;
            padding: 40px;
            max-width: 700px;
            width: 100%;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(138, 43, 226, 0.3);
        }
        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, #8a2be2, #00c896);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        .badge {
            display: inline-block;
            background: linear-gradient(90deg, #8a2be2, #00c896);
            color: white;
            padding: 8px 20px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 0.9rem;
            margin-bottom: 25px;
        }
        .feature-list {
            list-style: none;
            margin: 25px 0;
        }
        .feature-list li {
            padding: 12px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            color: #f8f9fa;
            display: flex;
            align-items: center;
        }
        .feature-list li:last-child {
            border-bottom: none;
        }
        .check-icon {
            color: #00c896;
            margin-right: 15px;
            font-size: 1.2rem;
        }
        .footer {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
            color: #6c757d;
            font-size: 0.9rem;
        }
        .footer a {
            color: #00c896;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .status {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }
        .status-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #00c896;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🔒 DevSecOps Pipeline</h1>
        <span class="badge">Security Automated • Shift Left</span>
        
        <p style="color: #f8f9fa; margin-bottom: 20px; font-size: 1.1rem;">
            Pipeline de seguridad automatizado que demuestra la integración de herramientas 
            SAST, SCA y Container Security en el ciclo de desarrollo.
        </p>
        
        <ul class="feature-list">
            <li>
                <span class="check-icon">✅</span>
                <span><strong>Gitleaks</strong> - Detección de secretos y credenciales expuestas</span>
            </li>
            <li>
                <span class="check-icon">✅</span>
                <span><strong>Bandit</strong> - Análisis estático de seguridad (SAST) para Python</span>
            </li>
            <li>
                <span class="check-icon">✅</span>
                <span><strong>Safety</strong> - Auditoría de dependencias con vulnerabilidades conocidas</span>
            </li>
            <li>
                <span class="check-icon">✅</span>
                <span><strong>Trivy</strong> - Escaneo de vulnerabilidades en imágenes Docker</span>
            </li>
        </ul>
        
        <div class="status">
            <span class="status-dot"></span>
            <span style="color: #6c757d;">Pipeline activo • Último escaneo: exitoso</span>
        </div>
        
        <div class="footer">
            <p><strong>Leidy Diana Principe Quispe</strong> • Especialista en Ciberseguridad</p>
            <p>
                📧 <a href="mailto:dprincipe.q@gmail.com">dprincipe.q@gmail.com</a> • 
                🔗 <a href="https://www.linkedin.com/in/leidy-diana-principe-quispe-8ba739131/" target="_blank">LinkedIn</a> •
                💻 <a href="https://github.com/DinoDiana-98" target="_blank">GitHub</a>
            </p>
            <p style="margin-top: 15px;">
                <span style="background: rgba(0,200,150,0.1); padding: 5px 12px; border-radius: 20px;">
                    🎯 Portafolio de Ciberseguridad 2026
                </span>
            </p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return {
        "status": "healthy",
        "security_pipeline": "active",
        "tools": ["Gitleaks", "Bandit", "Safety", "Trivy"],
        "author": "Leidy Diana Principe Quispe"
    }

@app.route('/version')
def version():
    return {
        "app": "DevSecOps Demo",
        "version": "2.0.0",
        "security_checks": "enabled"
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
