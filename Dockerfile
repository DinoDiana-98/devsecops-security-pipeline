# Imagen 
FROM python:3.11-alpine

# Etiquetas para documentación
LABEL maintainer="Leidy Diana Principe Quispe <dprincipe.q@gmail.com>"
LABEL description="DevSecOps Demo App - Security Pipeline Portfolio"
LABEL version="2.0.0"
LABEL org.opencontainers.image.source="https://github.com/DinoDiana-98/devsecops-security-pipeline"

# Instalar dependencias del sistema necesarias
RUN apk add --no-cache curl

# Crear directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY app.py .

# Crear usuario no-root 
RUN addgroup -g 1001 -S appgroup && \
    adduser -u 1001 -S appuser -G appgroup && \
    chown -R appuser:appgroup /app

# Cambiar a usuario no-root
USER appuser

# Exponer puerto
EXPOSE 5000

# Healthcheck para monitoreo
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Comando de inicio
CMD ["python", "app.py"]
