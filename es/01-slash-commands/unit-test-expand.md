---
name: Expand Unit Tests
description: Increase test coverage by targeting untested branches and edge cases
tags: testing, coverage, unit-tests
---

# Expandir Unit Tests

Expandir unit tests existentes adaptados al framework de testing del proyecto:

1. **Analizar cobertura**: Ejecutar reporte de cobertura para identificar branches no testeados, casos limite y areas de baja cobertura
2. **Identificar gaps**: Revisar codigo buscando branches logicos, caminos de error, condiciones limite, inputs nulos/vacios
3. **Escribir tests** usando el framework del proyecto:
   - Jest/Vitest/Mocha (JavaScript/TypeScript)
   - pytest/unittest (Python)
   - Go testing/testify (Go)
   - Rust test framework (Rust)
4. **Apuntar a escenarios especificos**:
   - Manejo de errores y excepciones
   - Valores limite (min/max, vacio, nulo)
   - Casos limite y casos esquina
   - Transiciones de estado y efectos secundarios
5. **Verificar mejora**: Ejecutar cobertura de nuevo, confirmar incremento medible

Presentar solo los bloques de codigo de tests nuevos. Seguir patrones y convenciones de naming existentes.

---

**Ultima Actualizacion**: Abril 2026
