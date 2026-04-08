---
name: blog-draft
description: Draft a blog post from ideas and resources. Use when users want to write a blog post, create content from research, or draft articles. Guides through research, brainstorming, outlining, and iterative drafting with version control.
---

## Entrada del usuario

```text
$ARGUMENTS
```

**DEBES** considerar la entrada del usuario antes de continuar. El usuario debe proporcionar:
- **Idea/Tema**: El concepto principal o tema del blog post
- **Recursos**: URLs, archivos o referencias de investigación (opcional pero recomendado)
- **Audiencia objetivo**: Para quién es el blog post (opcional)
- **Tono/Estilo**: Formal, casual, técnico, etc. (opcional)

**IMPORTANTE**: Si el usuario está pidiendo actualizaciones a un **blog post existente**, omite los pasos 0-8 y comienza directamente en el **Paso 9**. Lee primero los archivos de borrador existentes y luego continúa con el proceso de iteración.

## Flujo de ejecución

Sigue estos pasos de forma secuencial. **No omitas pasos ni avances sin la aprobación del usuario donde se indica.**

### Paso 0: Crear carpeta del proyecto

1. Genera un nombre de carpeta con el formato: `YYYY-MM-DD-short-topic-name`
   - Usa la fecha de hoy
   - Crea un slug corto y amigable para URLs a partir del tema (minúsculas, guiones, máximo 5 palabras)

2. Creá la estructura de carpetas:
   ```
   blog-posts/
   └── YYYY-MM-DD-short-topic-name/
       └── resources/
   ```

3. Confirmá la creación de la carpeta con el usuario antes de continuar.

### Paso 1: Investigación y recopilación de recursos

1. Crea la subcarpeta `resources/` dentro del directorio del blog post

2. Para cada recurso proporcionado:
   - **URLs**: Descarga y guarda la información clave en `resources/` como archivos markdown
   - **Archivos**: Lee y resume en `resources/`
   - **Temas**: Usa búsqueda web para recopilar información actualizada

3. Para cada recurso, crea un archivo de resumen en `resources/`:
   - `resources/source-1-[short-name].md`
   - `resources/source-2-[short-name].md`
   - etc.

4. Cada resumen debe incluir:
   ```markdown
   # Source: [Title/URL]

   ## Key Points
   - Point 1
   - Point 2

   ## Relevant Quotes/Data
   - Quote or statistic 1
   - Quote or statistic 2

   ## How This Relates to Topic
   Brief explanation of relevance
   ```

5. Presenta el resumen de la investigación al usuario.

### Paso 2: Lluvia de ideas y aclaración

1. Basándote en la idea y los recursos investigados, presenta:
   - **Temas principales** identificados en la investigación
   - **Ángulos posibles** para el blog post
   - **Puntos clave** que deberían cubrirse
   - **Brechas** de información que necesitan aclaración

2. Haz preguntas aclaratorias:
   - ¿Cuál es el mensaje principal que quieres que los lectores se lleven?
   - ¿Hay puntos específicos de la investigación que quieras enfatizar?
   - ¿Cuál es la extensión objetivo? (corto: 500-800 palabras, medio: 1000-1500, largo: 2000+)
   - ¿Hay puntos que quieras excluir?

3. **Esperá las respuestas del usuario antes de continuar.**

### Paso 3: Proponer el esquema

1. Creá un esquema estructurado que incluya:

   ```markdown
   # Blog Post Outline: [Title]

   ## Meta Information
   - **Target Audience**: [who]
   - **Tone**: [style]
   - **Target Length**: [word count]
   - **Main Takeaway**: [key message]

   ## Proposed Structure

   ### Hook/Introduction
   - Opening hook idea
   - Context setting
   - Thesis statement

   ### Section 1: [Title]
   - Key point A
   - Key point B
   - Supporting evidence from [source]

   ### Section 2: [Title]
   - Key point A
   - Key point B

   [Continue for all sections...]

   ### Conclusion
   - Summary of key points
   - Call to action or final thought

   ## Sources to Cite
   - Source 1
   - Source 2
   ```

2. Presenta el esquema al usuario y **pide aprobación o modificaciones**.

### Paso 4: Guardar el esquema aprobado

1. Una vez que el usuario apruebe el esquema, guárdalo en `OUTLINE.md` dentro de la carpeta del blog post.

2. Confirmá que el esquema fue guardado.

### Paso 5: Commit del esquema (si está en un repositorio git)

1. Verifica si el directorio actual es un repositorio git.

2. Si lo es:
   - Stagear los nuevos archivos: carpeta del blog post, recursos y OUTLINE.md
   - Crear el commit con el mensaje: `docs: Add outline for blog post - [topic-name]`
   - Push al remoto

3. Si no es un repositorio git, omite este paso e informa al usuario.

### Paso 6: Escribir el borrador

1. Basándote en el esquema aprobado, escribe el borrador completo del blog post.

2. Sigue la estructura de OUTLINE.md exactamente.

3. Incluye:
   - Introducción atractiva con un gancho
   - Encabezados de sección claros
   - Evidencia y ejemplos de la investigación
   - Transiciones fluidas entre secciones
   - Conclusión sólida con mensaje clave
   - **Citas**: Todas las comparaciones, estadísticas, datos y afirmaciones factuales DEBEN citar la fuente original

4. Guarda el borrador como `draft-v0.1.md` en la carpeta del blog post.

5. Formato:
   ```markdown
   # [Blog Post Title]

   *[Optional: subtitle or tagline]*

   [Full content with inline citations...]

   ---

   ## References
   - [1] Source 1 Title - URL or Citation
   - [2] Source 2 Title - URL or Citation
   - [3] Source 3 Title - URL or Citation
   ```

6. **Requisitos de citas**:
   - Cada dato, estadística o comparación DEBE tener una cita en línea
   - Usa referencias numeradas [1], [2], etc., o citas con nombre [Nombre de la fuente]
   - Vincula las citas a la sección de Referencias al final
   - Ejemplo: "Los estudios muestran que el 65% de los desarrolladores prefieren TypeScript [1]"
   - Ejemplo: "React supera a Vue en velocidad de renderizado en un 20% [React Benchmarks 2024]"

### Paso 7: Commit del borrador (si está en un repositorio git)

1. Verifica si estás en un repositorio git.

2. Si lo es:
   - Stagear el archivo de borrador
   - Crear el commit con el mensaje: `docs: Add draft v0.1 for blog post - [topic-name]`
   - Push al remoto

3. Si no es un repositorio git, omite e informa al usuario.

### Paso 8: Presentar el borrador para revisión

1. Presenta el contenido del borrador al usuario.

2. Pide retroalimentación:
   - ¿Impresión general?
   - ¿Secciones que necesitan expansión o reducción?
   - ¿Ajustes de tono necesarios?
   - ¿Información faltante?
   - ¿Ediciones o reescrituras específicas?

3. **Esperá la respuesta del usuario.**

### Paso 9: Iterar o finalizar

**Si el usuario solicita cambios:**
1. Anota todas las modificaciones solicitadas
2. Vuelve al Paso 6 con los siguientes ajustes:
   - Incrementá el número de versión (v0.2, v0.3, etc.)
   - Incorporá toda la retroalimentación
   - Guardá como `draft-v[X.Y].md`
   - Repite los Pasos 7-8

**Si el usuario aprueba:**
1. Confirmá la versión final del borrador
2. Opcionalmente renombrá a `final.md` si el usuario lo solicita
3. Resumí el proceso de creación del blog post:
   - Total de versiones creadas
   - Cambios clave entre versiones
   - Recuento final de palabras
   - Archivos creados

## Seguimiento de versiones

Todos los borradores se conservan con versionado incremental:
- `draft-v0.1.md` - Borrador inicial
- `draft-v0.2.md` - Después de la primera ronda de retroalimentación
- `draft-v0.3.md` - Después de la segunda ronda de retroalimentación
- etc.

Esto permite rastrear la evolución del blog post y revertir si es necesario.

## Estructura de archivos de salida

```
blog-posts/
└── YYYY-MM-DD-topic-name/
    ├── resources/
    │   ├── source-1-name.md
    │   ├── source-2-name.md
    │   └── ...
    ├── OUTLINE.md
    ├── draft-v0.1.md
    ├── draft-v0.2.md (if iterations)
    └── draft-v0.3.md (if more iterations)
```

## Consejos para la calidad

- **Gancho**: Comienza con una pregunta, un dato sorprendente o un escenario identificable
- **Flujo**: Cada párrafo debe conectar con el siguiente
- **Evidencia**: Apoyá las afirmaciones con datos de la investigación
- **Citas**: SIEMPRE citá fuentes para:
  - Todas las estadísticas y datos (ej.: "Según [Fuente], el 75% de...")
  - Comparaciones entre productos, servicios o enfoques (ej.: "X funciona 2x más rápido que Y [Fuente]")
  - Afirmaciones factuales sobre tendencias del mercado, hallazgos de investigación o benchmarks
  - Usa citas en línea con el formato: [Nombre de la fuente] o [Autor, Año]
- **Voz**: Mantén un tono consistente en todo el texto
- **Extensión**: Respeta el recuento de palabras objetivo
- **Legibilidad**: Usa párrafos cortos y viñetas donde corresponda
- **CTA**: Terminá con un llamado a la acción claro o una pregunta que invite a reflexionar

## Notas

- Siempre esperá la aprobación del usuario en los puntos de control indicados
- Conservá todas las versiones de los borradores para tener un historial
- Usá búsqueda web para obtener información actualizada cuando se proporcionen URLs
- Si los recursos son insuficientes, pídele más al usuario o sugiere investigación adicional
- Adaptá el tono según la audiencia objetivo (técnica, general, empresarial, etc.)
