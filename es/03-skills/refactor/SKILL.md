---
name: code-refactor
description: Systematic code refactoring based on Martin Fowler's methodology. Use when users ask to refactor code, improve code structure, reduce technical debt, clean up legacy code, eliminate code smells, or improve code maintainability. This skill guides through a phased approach with research, planning, and safe incremental implementation.
---

# Skill de refactorización de código

Un enfoque sistemático para refactorizar código basado en la metodología de Martin Fowler en *Refactoring: Improving the Design of Existing Code* (2.ª edición). Este skill hace énfasis en cambios seguros e incrementales respaldados por tests.

> "Refactoring is the process of changing a software system in such a way that it does not alter the external behavior of the code yet improves its internal structure." — Martin Fowler

## Principios fundamentales

1. **Preservación del comportamiento**: El comportamiento externo debe permanecer sin cambios
2. **Pasos pequeños**: Realiza cambios mínimos y verificables
3. **Orientado a tests**: Los tests son la red de seguridad
4. **Continuo**: La refactorización es un proceso continuo, no un evento único
5. **Colaborativo**: Se requiere la aprobación del usuario en cada fase

## Resumen del flujo de trabajo

```
Phase 1: Research & Analysis
    ↓
Phase 2: Test Coverage Assessment
    ↓
Phase 3: Code Smell Identification
    ↓
Phase 4: Refactoring Plan Creation
    ↓
Phase 5: Incremental Implementation
    ↓
Phase 6: Review & Iteration
```

---

## Fase 1: Investigación y análisis

### Objetivos
- Entender la estructura y el propósito del codebase
- Identificar el alcance de la refactorización
- Recopilar contexto sobre los requisitos del negocio

### Preguntas para hacerle al usuario
Antes de empezar, aclarár:

1. **Alcance**: ¿Qué archivos/módulos/funciones necesitan refactorización?
2. **Objetivos**: ¿Qué problemas intentas resolver? (legibilidad, rendimiento, mantenibilidad)
3. **Restricciones**: ¿Hay alguna área que NO deba cambiarse?
4. **Presión de tiempo**: ¿Esto está bloqueando otro trabajo?
5. **Estado de los tests**: ¿Existen tests? ¿Están pasando?

### Acciones
- [ ] Lee y entiende el código objetivo
- [ ] Identifica dependencias e integraciones
- [ ] Documenta la arquitectura actual
- [ ] Anota los marcadores de deuda técnica existentes (TODOs, FIXMEs)

### Resultado
Presenta los hallazgos al usuario:
- Resumen de la estructura del código
- Áreas problemáticas identificadas
- Recomendaciones iniciales
- **Solicita aprobación para continuar**

---

## Fase 2: Evaluación de la cobertura de tests

### Por qué importan los tests
> "Refactoring without tests is like driving without a seatbelt." — Martin Fowler

Los tests son el **habilitador clave** de la refactorización segura. Sin ellos, corres el riesgo de introducir bugs.

### Pasos de evaluación

1. **Verifica si existen tests**
   ```bash
   # Look for test files
   find . -name "*test*" -o -name "*spec*" | head -20
   ```

2. **Ejecuta los tests existentes**
   ```bash
   # JavaScript/TypeScript
   npm test

   # Python
   pytest -v

   # Java
   mvn test
   ```

3. **Verifica la cobertura (si está disponible)**
   ```bash
   # JavaScript
   npm run test:coverage

   # Python
   pytest --cov=.
   ```

### Punto de decisión: Preguntarle al usuario

**Si los tests existen y pasan:**
- Procedé a la Fase 3

**Si los tests faltan o están incompletos:**
Presenta opciones:
1. Escribir tests primero (recomendado)
2. Agregar tests de forma incremental durante la refactorización
3. Proceder sin tests (riesgoso — requiere reconocimiento del usuario)

**Si los tests están fallando:**
- DETENTE. Arregla los tests que fallan antes de refactorizar
- Pregúntale al usuario: ¿Deberíamos arreglar los tests primero?

### Guías para escribir tests (si es necesario)

Para cada función que se refactorice, asegúrate de que los tests cubran:
- Camino feliz (operación normal)
- Casos límite (entradas vacías, null, límites)
- Escenarios de error (entradas inválidas, excepciones)

Usa el ciclo "red-green-refactor":
1. Escribir el test que falla (rojo)
2. Hacerlo pasar (verde)
3. Refactorizar

---

## Fase 3: Identificación de code smells

### ¿Qué son los code smells?
Síntomas de problemas más profundos en el código. No son bugs, sino indicadores de que el código podría mejorarse.

### Code smells comunes a verificar

Consulta [references/code-smells.md](references/code-smells.md) para el catálogo completo.

#### Referencia rápida

| Smell | Señales | Impacto |
|-------|---------|---------|
| **Long Method** | Métodos > 30-50 líneas | Difícil de entender, testear y mantener |
| **Duplicated Code** | La misma lógica en múltiples lugares | Los bug fixes deben hacerse en múltiples lugares |
| **Large Class** | Clase con demasiadas responsabilidades | Viola el Principio de Responsabilidad Única |
| **Feature Envy** | Un método usa más datos de otra clase | Encapsulación deficiente |
| **Primitive Obsession** | Uso excesivo de primitivos en lugar de objetos | Faltan conceptos del dominio |
| **Long Parameter List** | Métodos con 4+ parámetros | Difícil de llamar correctamente |
| **Data Clumps** | Los mismos ítems de datos aparecen juntos | Abstracción faltante |
| **Switch Statements** | Cadenas complejas de switch/if-else | Difícil de extender |
| **Speculative Generality** | Código "por si acaso" | Complejidad innecesaria |
| **Dead Code** | Código sin usar | Confusión, carga de mantenimiento |

### Pasos de análisis

1. **Análisis automatizado** (si hay scripts disponibles)
   ```bash
   python scripts/detect-smells.py <file>
   ```

2. **Revisión manual**
   - Recorré el código de forma sistemática
   - Anota cada smell con su ubicación y severidad
   - Categoriza por impacto (Crítico/Alto/Medio/Bajo)

3. **Priorización**
   Enfócate en los smells que:
   - Bloquean el desarrollo actual
   - Causan bugs o confusión
   - Afectan los caminos de código que más cambian

### Resultado: Informe de smells

Presenta al usuario:
- Lista de smells identificados con ubicaciones
- Evaluación de severidad para cada uno
- Orden de prioridad recomendado
- **Solicita aprobación sobre las prioridades**

---

## Fase 4: Creación del plan de refactorización

### Selección de refactorizaciones

Para cada smell, selecciona una refactorización apropiada del catálogo.

Consulta [references/refactoring-catalog.md](references/refactoring-catalog.md) para la lista completa.

#### Mapeo de smell a refactorización

| Code Smell | Refactorización(es) recomendada(s) |
|------------|-----------------------------------|
| Long Method | Extract Method, Replace Temp with Query |
| Duplicated Code | Extract Method, Pull Up Method, Form Template Method |
| Large Class | Extract Class, Extract Subclass |
| Feature Envy | Move Method, Move Field |
| Primitive Obsession | Replace Primitive with Object, Replace Type Code with Class |
| Long Parameter List | Introduce Parameter Object, Preserve Whole Object |
| Data Clumps | Extract Class, Introduce Parameter Object |
| Switch Statements | Replace Conditional with Polymorphism |
| Speculative Generality | Collapse Hierarchy, Inline Class, Remove Dead Code |
| Dead Code | Remove Dead Code |

### Estructura del plan

Usa el template en [templates/refactoring-plan.md](templates/refactoring-plan.md).

Para cada refactorización:
1. **Objetivo**: Qué código cambiará
2. **Smell**: Qué problema aborda
3. **Refactorización**: Qué técnica aplicar
4. **Pasos**: Micro-pasos detallados
5. **Riesgos**: Qué podría salir mal
6. **Rollback**: Cómo deshacerlo si es necesario

### Enfoque por fases

**CRÍTICO**: Introducí la refactorización gradualmente en fases.

**Fase A: Ganancias rápidas** (Bajo riesgo, alto valor)
- Renombra variables para mayor claridad
- Extrae código duplicado obvio
- Elimina código muerto

**Fase B: Mejoras estructurales** (Riesgo medio)
- Extrae métodos de funciones largas
- Introduce objetos de parámetros
- Mueve métodos a las clases apropiadas

**Fase C: Cambios arquitectónicos** (Mayor riesgo)
- Reemplaza condicionales con polimorfismo
- Extrae clases
- Introduce patrones de diseño

### Punto de decisión: Presentar el plan al usuario

Antes de la implementación:
- Muestra el plan de refactorización completo
- Explica cada fase y sus riesgos
- Obtén aprobación explícita para cada fase
- **Pregunta**: "¿Procedo con la Fase A?"

---

## Fase 5: Implementación incremental

### La regla de oro
> "Change → Test → Green? → Commit → Next step"

### Ritmo de implementación

Para cada paso de refactorización:

1. **Verificación previa**
   - Los tests están pasando (verde)
   - El código compila

2. **Realiza UN cambio pequeño**
   - Sigue la mecánica del catálogo
   - Mantén los cambios mínimos

3. **Verifica**
   - Ejecuta los tests inmediatamente
   - Verifica errores de compilación

4. **Si los tests pasan (verde)**
   - Haz un commit con un mensaje descriptivo
   - Pasa al siguiente paso

5. **Si los tests fallan (rojo)**
   - DETENTE inmediatamente
   - Deshaz el cambio
   - Analiza qué salió mal
   - Pregúntale al usuario si no está claro

### Estrategia de commits

Cada commit debe ser:
- **Atómico**: Un cambio lógico
- **Reversible**: Fácil de revertir
- **Descriptivo**: Mensaje de commit claro

Ejemplos de mensajes de commit:
```
refactor: Extract calculateTotal() from processOrder()
refactor: Rename 'x' to 'customerCount' for clarity
refactor: Remove unused validateOldFormat() method
```

### Reporte de progreso

Después de cada sub-fase, repórtale al usuario:
- Cambios realizados
- ¿Los tests siguen pasando?
- ¿Algún problema encontrado?
- **Pregunta**: "¿Continúo con el siguiente lote?"

---

## Fase 6: Revisión e iteración

### Lista de verificación post-refactorización

- [ ] Todos los tests pasando
- [ ] Sin nuevas advertencias/errores
- [ ] El código compila correctamente
- [ ] Comportamiento sin cambios (verificación manual)
- [ ] Documentación actualizada si es necesario
- [ ] El historial de commits está limpio

### Comparación de métricas

Ejecuta el análisis de complejidad antes y después:
```bash
python scripts/analyze-complexity.py <file>
```

Presenta las mejoras:
- Cambio en líneas de código
- Cambio en complejidad ciclomática
- Cambio en el índice de mantenibilidad

### Revisión del usuario

Presenta los resultados finales:
- Resumen de todos los cambios
- Comparación del código antes/después
- Mejoras en métricas
- Deuda técnica restante
- **Pregunta**: "¿Estás satisfecho con estos cambios?"

### Próximos pasos

Conversa con el usuario:
- ¿Smells adicionales a abordar?
- ¿Programar una refactorización de seguimiento?
- ¿Aplicar cambios similares en otros lugares?

---

## Guías importantes

### Cuándo DETENERSE y consultar

Siempre pausa y consulta al usuario cuando:
- No estés seguro sobre la lógica del negocio
- Un cambio podría afectar APIs externas
- La cobertura de tests es insuficiente
- Se necesita una decisión arquitectónica importante
- El nivel de riesgo aumenta
- Encuentres complejidad inesperada

### Reglas de seguridad

1. **Nunca refactorices sin tests** (salvo que el usuario reconozca explícitamente el riesgo)
2. **Nunca hagas cambios grandes** — divídelos en pasos pequeños
3. **Nunca omitas ejecutar los tests** después de cada cambio
4. **Nunca continúes si los tests fallan** — arregla o haz rollback primero
5. **Nunca asumas** — cuando tengas dudas, pregunta

### Qué NO hacer

- No combines refactorización con adición de funcionalidades
- No refactorices durante emergencias en producción
- No refactorices código que no entiendes
- No sobre-ingenierices — mantenerlo simple
- No refactorices todo a la vez

---

## Ejemplo de inicio rápido

### Escenario: Método largo con duplicación

**Antes:**
```javascript
function processOrder(order) {
  // 150 lines of code with:
  // - Duplicated validation logic
  // - Inline calculations
  // - Mixed responsibilities
}
```

**Pasos de refactorización:**

1. **Asegúrate de que existan tests** para processOrder()
2. **Extrae** la validación en validateOrder()
3. **Prueba** — debería pasar
4. **Extrae** el cálculo en calculateOrderTotal()
5. **Prueba** — debería pasar
6. **Extrae** la notificación en notifyCustomer()
7. **Prueba** — debería pasar
8. **Revisa** — processOrder() ahora orquesta 3 funciones claras

**Después:**
```javascript
function processOrder(order) {
  validateOrder(order);
  const total = calculateOrderTotal(order);
  notifyCustomer(order, total);
  return { order, total };
}
```

---

## Referencias

- [Catálogo de code smells](references/code-smells.md) - Lista completa de code smells
- [Catálogo de refactorizaciones](references/refactoring-catalog.md) - Técnicas de refactorización
- [Template de plan de refactorización](templates/refactoring-plan.md) - Template de planificación

## Scripts

- `scripts/analyze-complexity.py` - Analiza métricas de complejidad del código
- `scripts/detect-smells.py` - Detección automatizada de smells

## Historial de versiones

- v1.0.0 (2025-01-15): Lanzamiento inicial con metodología Fowler, enfoque por fases, puntos de consulta con el usuario
