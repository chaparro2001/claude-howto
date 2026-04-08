# Política de seguridad

## Descripción general

La seguridad del proyecto Claude How To es importante para nosotros. Este documento describe nuestras prácticas de seguridad y explica cómo reportar vulnerabilidades de manera responsable.

## Versiones soportadas

Proporcionamos actualizaciones de seguridad para las siguientes versiones:

| Versión | Estado | Soporte hasta |
|---------|--------|---------------|
| Última (main) | ✅ Activa | Actual + 6 meses |
| Versiones 1.x | ✅ Activa | Hasta la próxima versión mayor |

**Nota**: Como proyecto de guía educativa, nos enfocamos en mantener las mejores prácticas actuales y la seguridad de la documentación, en lugar del soporte tradicional por versiones. Las actualizaciones se aplican directamente al branch main.

## Prácticas de seguridad

### Seguridad del código

1. **Gestión de dependencias**
   - Todas las dependencias Python están fijadas en `requirements.txt`
   - Actualizaciones regulares mediante dependabot y revisión manual
   - Análisis de seguridad con Bandit en cada commit
   - Pre-commit hooks para verificaciones de seguridad

2. **Calidad del código**
   - El linting con Ruff detecta problemas comunes
   - La verificación de tipos con mypy previene vulnerabilidades relacionadas con tipos
   - Los pre-commit hooks hacen cumplir los estándares
   - Todos los cambios son revisados antes de hacer merge

3. **Control de acceso**
   - Protección de branch en el branch `main`
   - Revisiones requeridas antes del merge
   - Las verificaciones de estado deben pasar antes del merge
   - Acceso de escritura limitado al repositorio

### Seguridad de la documentación

1. **Sin secretos en los ejemplos**
   - Todas las claves de API en los ejemplos son marcadores de posición
   - Las credenciales nunca están hardcodeadas
   - Los archivos `.env.example` muestran las variables requeridas
   - Advertencias claras sobre la gestión de secretos

2. **Mejores prácticas de seguridad**
   - Los ejemplos demuestran patrones seguros
   - Las advertencias de seguridad están destacadas en la documentación
   - Links a guías de seguridad oficiales
   - El manejo de credenciales se discute en las secciones relevantes

3. **Revisión de contenido**
   - Toda la documentación es revisada para detectar problemas de seguridad
   - Consideraciones de seguridad en las guías de contribución
   - Validación de links y referencias externas

### Seguridad de dependencias

1. **Análisis**
   - Bandit analiza todo el código Python en busca de vulnerabilidades
   - Verificaciones de vulnerabilidades en dependencias mediante las alertas de seguridad de GitHub
   - Auditorías de seguridad manuales periódicas

2. **Actualizaciones**
   - Los parches de seguridad se aplican con prontitud
   - Las versiones mayores se evalúan cuidadosamente
   - El changelog incluye actualizaciones relacionadas con seguridad

3. **Transparencia**
   - Las actualizaciones de seguridad se documentan en los commits
   - Las divulgaciones de vulnerabilidades se manejan de manera responsable
   - Avisos de seguridad públicos cuando corresponde

## Reportar una vulnerabilidad

### Issues de seguridad que nos importan

Agradecemos los reportes sobre:
- **Vulnerabilidades de código** en scripts o ejemplos
- **Vulnerabilidades de dependencias** en paquetes Python
- **Problemas de criptografía** en cualquier ejemplo de código
- **Fallas de autenticación/autorización** en la documentación
- **Riesgos de exposición de datos** en ejemplos de configuración
- **Vulnerabilidades de inyección** (SQL, comandos, etc.)
- **Problemas de SSRF/XXE/traversal de rutas**

### Issues de seguridad fuera de alcance

Estos están fuera del alcance de este proyecto:
- Vulnerabilidades en Claude Code en sí mismo (reportar a Anthropic)
- Problemas con servicios o bibliotecas externas (reportar al upstream)
- Ingeniería social o educación de usuarios (no aplica a esta guía)
- Vulnerabilidades teóricas sin prueba de concepto
- Vulnerabilidades en dependencias reportadas a través de canales oficiales

## Cómo reportar

### Reporte privado (preferido)

**Para issues de seguridad sensibles, usar el reporte privado de vulnerabilidades de GitHub:**

1. Visitar: https://github.com/luongnv89/claude-howto/security/advisories
2. Hacer clic en "Report a vulnerability"
3. Completar los detalles de la vulnerabilidad
4. Incluir:
   - Descripción clara de la vulnerabilidad
   - Componente afectado (archivo, sección, ejemplo)
   - Impacto potencial
   - Pasos para reproducir (si aplica)
   - Corrección sugerida (si tenés una)

**Qué ocurre después:**
- Confirmaremos la recepción dentro de las 48 horas
- Investigaremos y evaluaremos la severidad
- Trabajaremos con vos para desarrollar una corrección
- Coordinaremos el cronograma de divulgación
- Te daremos crédito en el aviso de seguridad (a menos que prefieras el anonimato)

### Reporte público

Para issues no sensibles o los que ya son públicos:

1. **Abrir un GitHub Issue** con la etiqueta `security`
2. Incluir:
   - Título: `[SECURITY]` seguido de una breve descripción
   - Descripción detallada
   - Archivo o sección afectada
   - Impacto potencial
   - Corrección sugerida

## Proceso de respuesta a vulnerabilidades

### Evaluación (24 horas)

1. Confirmamos la recepción del reporte
2. Evaluamos la severidad usando [CVSS v3.1](https://www.first.org/cvss/v3.1/specification-document)
3. Determinamos si está dentro del alcance
4. Te contactamos con la evaluación inicial

### Desarrollo (1-7 días)

1. Desarrollamos una corrección
2. Revisamos y probamos la corrección
3. Creamos un aviso de seguridad
4. Preparamos las notas de la versión

### Divulgación (varía según la severidad)

**Crítica (CVSS 9.0-10.0)**
- Corrección publicada de inmediato
- Aviso público emitido
- Notificación anticipada de 24 horas a los reporteros

**Alta (CVSS 7.0-8.9)**
- Corrección publicada dentro de 48-72 horas
- Notificación anticipada de 5 días a los reporteros
- Aviso público al publicar

**Media (CVSS 4.0-6.9)**
- Corrección publicada en la próxima actualización regular
- Aviso público al publicar

**Baja (CVSS 0.1-3.9)**
- Corrección incluida en la próxima actualización regular
- Aviso al publicar

### Publicación

Publicamos avisos de seguridad que incluyen:
- Descripción de la vulnerabilidad
- Componentes afectados
- Evaluación de severidad (puntuación CVSS)
- Versión de corrección
- Soluciones alternativas (si aplica)
- Crédito al reportero (con su permiso)

## Mejores prácticas para los reporteros

### Antes de reportar

- **Verificar el issue**: ¿Podés reproducirlo de manera consistente?
- **Buscar issues existentes**: ¿Ya fue reportado?
- **Revisar la documentación**: ¿Hay orientación sobre el uso seguro?
- **Probar la corrección**: ¿Funciona la corrección que sugerís?

### Al reportar

- **Ser específico**: Proporcionar rutas de archivo exactas y números de línea
- **Incluir contexto**: ¿Por qué es esto un issue de seguridad?
- **Mostrar el impacto**: ¿Qué podría hacer un atacante?
- **Proporcionar pasos**: ¿Cómo podemos reproducirlo?
- **Sugerir correcciones**: ¿Cómo lo corregirías?

### Después de reportar

- **Ser paciente**: Tenemos recursos limitados
- **Ser receptivo**: Responder rápidamente a las preguntas de seguimiento
- **Mantener la confidencialidad**: No divulgar públicamente antes de la corrección
- **Respetar la coordinación**: Seguir nuestro cronograma de divulgación

## Encabezados y configuración de seguridad

### Seguridad del repositorio

- **Protección de branch**: El branch main requiere 2 aprobaciones para los cambios
- **Verificaciones de estado**: Todas las verificaciones de CI/CD deben pasar
- **CODEOWNERS**: Revisores designados para archivos clave
- **Commits firmados**: Recomendado para los colaboradores

### Seguridad del desarrollo

```bash
# Instalar pre-commit hooks
pre-commit install

# Ejecutar análisis de seguridad localmente
bandit -c pyproject.toml -r scripts/
mypy scripts/ --ignore-missing-imports
ruff check scripts/
```

### Seguridad de dependencias

```bash
# Verificar vulnerabilidades conocidas
pip install safety
safety check

# O usar pip-audit
pip install pip-audit
pip-audit
```

## Pautas de seguridad para colaboradores

### Al escribir ejemplos

1. **Nunca dejar secretos hardcodeados**
   ```python
   # ❌ Malo
   api_key = "sk-1234567890"

   # ✅ Bueno
   api_key = os.getenv("API_KEY")
   ```

2. **Advertir sobre implicaciones de seguridad**
   ```markdown
   ⚠️ **Security Note**: Never commit `.env` files to git.
   Add to `.gitignore` immediately.
   ```

3. **Usar valores seguros por defecto**
   - Activar la autenticación por defecto
   - Usar HTTPS donde corresponda
   - Validar y sanitizar las entradas
   - Usar consultas parametrizadas

4. **Documentar consideraciones de seguridad**
   - Explicar por qué importa la seguridad
   - Mostrar patrones seguros vs. inseguros
   - Enlazar a fuentes autorizadas
   - Incluir advertencias de manera prominente

### Al revisar contribuciones

1. **Verificar secretos expuestos**
   - Analizar en busca de patrones comunes (api_key=, password=)
   - Revisar archivos de configuración
   - Verificar variables de entorno

2. **Verificar prácticas de codificación segura**
   - Sin credenciales hardcodeadas
   - Validación adecuada de entradas
   - Autenticación/autorización segura
   - Manejo seguro de archivos

3. **Probar las implicaciones de seguridad**
   - ¿Se puede hacer un mal uso de esto?
   - ¿Cuál es el peor caso?
   - ¿Hay casos extremos?

## Recursos de seguridad

### Estándares oficiales
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [CVSS Calculator](https://www.first.org/cvss/calculator/3.1)

### Seguridad en Python
- [Python Security Advisories](https://www.python.org/dev/security/)
- [PyPI Security](https://pypi.org/help/#security)
- [Bandit Documentation](https://bandit.readthedocs.io/)

### Gestión de dependencias
- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)
- [GitHub Security Alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)

### Seguridad general
- [Anthropic Security](https://www.anthropic.com/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

## Archivo de avisos de seguridad

Los avisos de seguridad anteriores están disponibles en la pestaña [GitHub Security Advisories](https://github.com/luongnv89/claude-howto/security/advisories).

## Contacto

Para preguntas relacionadas con la seguridad o para discutir prácticas de seguridad:

1. **Reporte privado de seguridad**: Usar el reporte privado de vulnerabilidades de GitHub
2. **Preguntas generales de seguridad**: Abrir una discusión con la etiqueta `[SECURITY]`
3. **Comentarios sobre la política de seguridad**: Crear un issue con la etiqueta `security`

## Agradecimientos

Agradecemos a los investigadores de seguridad y miembros de la comunidad que ayudan a mantener este proyecto seguro. Los colaboradores que reportan vulnerabilidades de manera responsable serán reconocidos en nuestros avisos de seguridad (a menos que prefieran el anonimato).

## Actualizaciones de la política

Esta política de seguridad se revisa y actualiza:
- Cuando se descubren nuevas vulnerabilidades
- Cuando evolucionan las mejores prácticas de seguridad
- Cuando cambia el alcance del proyecto
- Como mínimo, de manera anual

**Ultima Actualizacion**: Enero 2026
**Próxima revisión**: Enero 2027

---

Gracias por ayudar a mantener seguro Claude How To! 🔒
