---
name: code-review-specialist
description: Comprehensive code review with security, performance, and quality analysis. Use when users ask to review code, analyze code quality, evaluate pull requests, or mention code review, security analysis, or performance optimization.
---

# Skill de revisión de código

Este skill provee capacidades completas de revisión de código, con foco en:

1. **Análisis de seguridad**
   - Problemas de autenticación/autorización
   - Riesgos de exposición de datos
   - Vulnerabilidades de inyección
   - Debilidades criptográficas
   - Logging de datos sensibles

2. **Revisión de rendimiento**
   - Eficiencia de algoritmos (análisis Big O)
   - Optimización de memoria
   - Optimización de consultas a base de datos
   - Oportunidades de caché
   - Problemas de concurrencia

3. **Calidad del código**
   - Principios SOLID
   - Patrones de diseño
   - Convenciones de nomenclatura
   - Documentación
   - Cobertura de tests

4. **Mantenibilidad**
   - Legibilidad del código
   - Tamaño de las funciones (debe ser < 50 líneas)
   - Complejidad ciclomática
   - Gestión de dependencias
   - Type safety

## Template de revisión

Para cada fragmento de código revisado, proporcioná:

### Resumen
- Evaluación general de calidad (1-5)
- Cantidad de hallazgos clave
- Áreas de prioridad recomendadas

### Problemas críticos (si los hay)
- **Problema**: Descripción clara
- **Ubicación**: Archivo y número de línea
- **Impacto**: Por qué esto importa
- **Severidad**: Crítico/Alto/Medio
- **Solución**: Ejemplo de código

### Hallazgos por categoría

#### Seguridad (si se encuentran problemas)
Listá las vulnerabilidades de seguridad con ejemplos

#### Rendimiento (si se encuentran problemas)
Listá los problemas de rendimiento con análisis de complejidad

#### Calidad (si se encuentran problemas)
Listá los problemas de calidad del código con sugerencias de refactorización

#### Mantenibilidad (si se encuentran problemas)
Listá los problemas de mantenibilidad con mejoras propuestas

## Historial de versiones

- v1.0.0 (2024-12-10): Lanzamiento inicial con análisis de seguridad, rendimiento, calidad y mantenibilidad
