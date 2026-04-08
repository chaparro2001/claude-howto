<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Checkpoints y Rewind

Los checkpoints te permiten guardar el estado de la conversación y volver a puntos anteriores en tu sesión de Claude Code. Esto es invaluable para explorar diferentes enfoques, recuperarte de errores o comparar soluciones alternativas.

## Descripcion general

Los checkpoints te permiten guardar el estado de la conversación y volver a puntos anteriores, habilitando la experimentacion segura y la exploracion de multiples enfoques. Son instantaneas del estado de tu conversacion que incluyen:
- Todos los mensajes intercambiados
- Modificaciones de archivos realizadas
- Historial de uso de herramientas
- Contexto de la sesion

Los checkpoints son invaluables cuando exploramos diferentes enfoques, nos recuperamos de errores o comparamos soluciones alternativas.

## Conceptos clave

| Concepto | Descripcion |
|---------|-------------|
| **Checkpoint** | Instantanea del estado de la conversacion que incluye mensajes, archivos y contexto |
| **Rewind** | Volver a un checkpoint anterior, descartando los cambios posteriores |
| **Branch Point** | Checkpoint desde el cual se exploran multiples enfoques |

## Acceder a los checkpoints

Podes acceder y gestionar los checkpoints de dos maneras principales:

### Usando el atajo de teclado
Presiona `Esc` dos veces (`Esc` + `Esc`) para abrir la interfaz de checkpoints y navegar por los guardados.

### Usando slash command
Usa el comando `/rewind` (alias: `/checkpoint`) para acceso rapido:

```bash
# Abrir la interfaz de rewind
/rewind

# O usar el alias
/checkpoint
```

## Opciones de Rewind

Cuando hacemos rewind, se presenta un menu con cinco opciones:

1. **Restore code and conversation** -- Revertir tanto los archivos como los mensajes a ese checkpoint
2. **Restore conversation** -- Rebobinar solo los mensajes, manteniendo el codigo actual tal como esta
3. **Restore code** -- Revertir solo los cambios de archivos, conservando el historial completo de la conversacion
4. **Summarize from here** -- Comprimir la conversacion desde este punto hacia adelante en un resumen generado por IA, liberando espacio en la ventana de contexto. Los mensajes anteriores al punto seleccionado se mantienen intactos. No se modifica ningun archivo en disco. Los mensajes originales se conservan en el transcript de la sesion. Opcionalmente podes dar instrucciones para enfocar el resumen en temas especificos.
5. **Never mind** -- Cancelar y volver al estado actual

> **Nota**: Despues de restaurar la conversacion o resumirla, el prompt original del mensaje seleccionado se restaura en el campo de entrada para que puedas reenviarlo o editarlo.

## Checkpoints automaticos

Claude Code crea checkpoints automaticamente:

- **Con cada prompt de usuario** - Se crea un nuevo checkpoint con cada entrada del usuario
- **Persistentes** - Los checkpoints persisten entre sesiones
- **Limpieza automatica** - Los checkpoints se limpian automaticamente despues de 30 dias

Esto significa que siempre podes volver a cualquier punto anterior de tu conversacion, desde hace unos minutos hasta dias atras.

## Casos de uso

| Escenario | Workflow |
|----------|----------|
| **Explorar enfoques** | Guardar → Intentar A → Guardar → Rewind → Intentar B → Comparar |
| **Refactorizacion segura** | Guardar → Refactorizar → Probar → Si falla: Rewind |
| **Pruebas A/B** | Guardar → Diseno A → Guardar → Rewind → Diseno B → Comparar |
| **Recuperacion de errores** | Detectar problema → Rewind al ultimo estado bueno |

## Uso de checkpoints

### Ver y hacer rewind

Presiona `Esc` dos veces o usa `/rewind` para abrir el navegador de checkpoints. Veras una lista de todos los checkpoints disponibles con marcas de tiempo. Selecciona cualquier checkpoint para volver a ese estado.

### Detalles del checkpoint

Cada checkpoint muestra:
- Marca de tiempo de cuando fue creado
- Archivos que fueron modificados
- Cantidad de mensajes en la conversacion
- Herramientas que se usaron

## Ejemplos practicos

### Ejemplo 1: Explorar diferentes enfoques

```
User: Let's add a caching layer to the API

Claude: I'll add Redis caching to your API endpoints...
[Makes changes at checkpoint A]

User: Actually, let's try in-memory caching instead

Claude: I'll rewind to explore a different approach...
[User presses Esc+Esc and rewinds to checkpoint A]
[Implements in-memory caching at checkpoint B]

User: Now I can compare both approaches
```

### Ejemplo 2: Recuperarse de errores

```
User: Refactor the authentication module to use JWT

Claude: I'll refactor the authentication module...
[Makes extensive changes]

User: Wait, that broke the OAuth integration. Let's go back.

Claude: I'll help you rewind to before the refactoring...
[User presses Esc+Esc and selects the checkpoint before the refactor]

User: Let's try a more conservative approach this time
```

### Ejemplo 3: Experimentacion segura

```
User: Let's try rewriting this in a functional style
[Creates checkpoint before experiment]

Claude: [Makes experimental changes]

User: The tests are failing. Let's rewind.
[User presses Esc+Esc and rewinds to the checkpoint]

Claude: I've rewound the changes. Let's try a different approach.
```

### Ejemplo 4: Ramificar enfoques

```
User: I want to compare two database designs
[Takes note of checkpoint - call it "Start"]

Claude: I'll create the first design...
[Implements Schema A]

User: Now let me go back and try the second approach
[User presses Esc+Esc and rewinds to "Start"]

Claude: Now I'll implement Schema B...
[Implements Schema B]

User: Great! Now I have both schemas to choose from
```

## Retencion de checkpoints

Claude Code gestiona automaticamente tus checkpoints:

- Los checkpoints se crean automaticamente con cada prompt de usuario
- Los checkpoints antiguos se retienen hasta 30 dias
- Los checkpoints se limpian automaticamente para evitar un crecimiento ilimitado del almacenamiento

## Patrones de workflow

### Estrategia de ramificacion para exploracion

Al explorar multiples enfoques:

```
1. Start with initial implementation → Checkpoint A
2. Try Approach 1 → Checkpoint B
3. Rewind to Checkpoint A
4. Try Approach 2 → Checkpoint C
5. Compare results from B and C
6. Choose best approach and continue
```

### Patron de refactorizacion segura

Al hacer cambios significativos:

```
1. Current state → Checkpoint (auto)
2. Start refactoring
3. Run tests
4. If tests pass → Continue working
5. If tests fail → Rewind and try different approach
```

## Buenas practicas

Como los checkpoints se crean automaticamente, podes concentrarte en tu trabajo sin preocuparte por guardar el estado manualmente. Sin embargo, tene en cuenta estas practicas:

### Uso efectivo de checkpoints

✅ **Hacer:**
- Revisar los checkpoints disponibles antes de hacer rewind
- Usar rewind cuando quieras explorar diferentes direcciones
- Conservar checkpoints para comparar diferentes enfoques
- Entender que hace cada opcion de rewind (restore code and conversation, restore conversation, restore code, o summarize)

❌ **No hacer:**
- Depender solo de los checkpoints para preservar codigo
- Esperar que los checkpoints rastreen cambios externos del sistema de archivos
- Usar checkpoints como sustituto de los commits de git

## Configuracion

Los checkpoints son un comportamiento predeterminado integrado en Claude Code y no requieren ninguna configuracion para habilitarse. Cada prompt de usuario crea automaticamente un checkpoint.

La unica configuracion relacionada con checkpoints es `cleanupPeriodDays`, que controla cuanto tiempo se retienen las sesiones y checkpoints:

```json
{
  "cleanupPeriodDays": 30
}
```

- `cleanupPeriodDays`: Cantidad de dias para retener el historial de sesiones y checkpoints (predeterminado: `30`)

## Limitaciones

Los checkpoints tienen las siguientes limitaciones:

- **Los cambios de comandos Bash NO se rastrean** - Operaciones como `rm`, `mv`, `cp` en el sistema de archivos no se capturan en los checkpoints
- **Los cambios externos NO se rastrean** - Los cambios realizados fuera de Claude Code (en tu editor, terminal, etc.) no se capturan
- **No reemplazan el control de versiones** - Usa git para cambios permanentes y auditables en tu base de codigo

## Solucion de problemas

### Checkpoints faltantes

**Problema**: No se encuentra el checkpoint esperado

**Solucion**:
- Verificar si los checkpoints fueron eliminados
- Revisar el espacio en disco
- Asegurarse de que `cleanupPeriodDays` sea suficientemente alto (predeterminado: 30 dias)

### Rewind fallido

**Problema**: No se puede hacer rewind al checkpoint

**Solucion**:
- Asegurarse de que no haya cambios sin commit que generen conflictos
- Verificar si el checkpoint esta corrompido
- Intentar hacer rewind a un checkpoint diferente

## Integracion con Git

Los checkpoints complementan (pero no reemplazan) a git:

| Caracteristica | Git | Checkpoints |
|---------|-----|-------------|
| Alcance | Sistema de archivos | Conversacion + archivos |
| Persistencia | Permanente | Basada en sesion |
| Granularidad | Commits | Cualquier punto |
| Velocidad | Mas lento | Instantaneo |
| Compartir | Si | Limitado |

Usa ambos juntos:
1. Usa checkpoints para experimentacion rapida
2. Usa commits de git para cambios finalizados
3. Crea un checkpoint antes de operaciones git
4. Haz commit de los estados de checkpoint exitosos en git

## Guia de inicio rapido

### Workflow basico

1. **Trabaja normalmente** - Claude Code crea checkpoints automaticamente
2. **Queres volver?** - Presiona `Esc` dos veces o usa `/rewind`
3. **Elige el checkpoint** - Selecciona de la lista para hacer rewind
4. **Selecciona que restaurar** - Elige entre restore code and conversation, restore conversation, restore code, summarize from here, o cancelar
5. **Continua trabajando** - Estas de vuelta en ese punto

### Atajos de teclado

- **`Esc` + `Esc`** - Abrir el navegador de checkpoints
- **`/rewind`** - Forma alternativa de acceder a los checkpoints
- **`/checkpoint`** - Alias de `/rewind`

## Saber cuando hacer rewind: monitoreo del contexto

Los checkpoints te permiten volver atras, pero ?como saber *cuando* deberias hacerlo? A medida que la conversacion crece, la ventana de contexto de Claude se llena y la calidad del modelo se degrada silenciosamente. Es posible que estes enviando codigo de un modelo "medio ciego" sin darte cuenta.

**[cc-context-stats](https://github.com/luongnv89/cc-context-stats)** resuelve esto agregando **zonas de contexto** en tiempo real a la barra de estado de Claude Code. Rastrea en que parte de la ventana de contexto te encontras, desde **Plan** (verde, seguro para planificar y codificar) pasando por **Code** (amarillo, evitar iniciar nuevos planes) hasta **Dump** (naranja, terminar y hacer rewind). Cuando ves el cambio de zona, sabes que es hora de hacer checkpoint y empezar de nuevo en lugar de continuar con una salida degradada.

## Conceptos relacionados

- **[Funcionalidades avanzadas](../09-advanced-features/)** - Modo de planificacion y otras capacidades avanzadas
- **[Gestion de memoria](../02-memory/)** - Manejo del historial de conversacion y contexto
- **[Slash Commands](../01-slash-commands/)** - Atajos invocados por el usuario
- **[Hooks](../06-hooks/)** - Automatizacion basada en eventos
- **[Plugins](../07-plugins/)** - Paquetes de extension incluidos

## Recursos adicionales

- [Documentacion oficial de Checkpointing](https://code.claude.com/docs/en/checkpointing)
- [Guia de funcionalidades avanzadas](../09-advanced-features/) - Pensamiento extendido y otras capacidades

## Resumen

Los checkpoints son una funcion automatica de Claude Code que te permite explorar diferentes enfoques de forma segura sin miedo a perder el trabajo. Cada prompt de usuario crea un nuevo checkpoint automaticamente, por lo que podes volver a cualquier punto anterior de tu sesion.

Beneficios clave:
- Experimenta libremente con multiples enfoques
- Recuperate rapidamente de errores
- Compara diferentes soluciones en paralelo
- Integracion segura con sistemas de control de versiones

Recuerda: los checkpoints no reemplazan a git. Usa checkpoints para experimentacion rapida y git para cambios permanentes en el codigo.

---
**Ultima Actualizacion**: Abril 2026
**Claude Code Version**: 2.1+
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
