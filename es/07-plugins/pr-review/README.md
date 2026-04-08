<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Plugin PR Review

Workflow completo de revision de PR con verificaciones de seguridad, testing y documentacion.

## Funcionalidades

✅ Analisis de seguridad
✅ Verificacion de cobertura de tests
✅ Verificacion de documentacion
✅ Evaluacion de calidad de codigo
✅ Analisis de impacto en rendimiento

## Instalacion

```bash
/plugin install pr-review
```

## Que incluye

### Slash Commands
- `/review-pr` - Revision completa de PR
- `/check-security` - Revision enfocada en seguridad
- `/check-tests` - Analisis de cobertura de tests

### Subagentes
- `security-reviewer` - Deteccion de vulnerabilidades de seguridad
- `test-checker` - Analisis de cobertura de tests
- `performance-analyzer` - Evaluacion de impacto en rendimiento

### Servidores MCP
- Integracion con GitHub para datos del PR

### Hooks
- `pre-review.js` - Validacion previa a la revision

## Uso

### Revision basica de PR
```
/review-pr
```

### Solo verificacion de seguridad
```
/check-security
```

### Verificacion de cobertura de tests
```
/check-tests
```

## Requisitos

- Claude Code 1.0+
- Acceso a GitHub
- Repositorio Git

## Configuracion

Configurar tu token de GitHub:
```bash
export GITHUB_TOKEN="your_github_token"
```

## Ejemplo de workflow

```
User: /review-pr

Claude:
1. Runs pre-review hook (validates git repo)
2. Fetches PR data via GitHub MCP
3. Delegates security review to security-reviewer subagent
4. Delegates testing to test-checker subagent
5. Delegates performance to performance-analyzer subagent
6. Synthesizes all findings
7. Provides comprehensive review report

Result:
✅ Security: No critical issues found
⚠️  Testing: Coverage is 65%, recommend 80%+
✅ Performance: No significant impact
📝 Recommendations: Add tests for edge cases
```
