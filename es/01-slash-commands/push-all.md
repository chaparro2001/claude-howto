---
description: Stage all changes, create commit, and push to remote (use with caution)
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# Commit y Push de Todo

**PRECAUCION**: Agrega TODOS los cambios al stage, hace commit y push al remoto. Usar solo cuando estes seguro de que todos los cambios van juntos.

## Workflow

### 1. Analizar Cambios

Ejecutar en paralelo:

- `git status` - Mostrar archivos modificados/agregados/eliminados/sin trackear
- `git diff --stat` - Mostrar estadisticas de cambios
- `git log -1 --oneline` - Mostrar commit reciente para estilo de mensaje

### 2. Verificaciones de Seguridad

**DETENER y ADVERTIR si se detecta:**

- Secretos: `.env*`, `*.key`, `*.pem`, `credentials.json`, `secrets.yaml`, `id_rsa`, `*.p12`, `*.pfx`, `*.cer`
- Claves API: Cualquier variable `*_API_KEY`, `*_SECRET`, `*_TOKEN` con valores reales (no placeholders como `your-api-key`, `xxx`, `placeholder`)
- Archivos grandes: `>10MB` sin Git LFS
- Artefactos de build: `node_modules/`, `dist/`, `build/`, `__pycache__/`, `*.pyc`, `.venv/`
- Archivos temporales: `.DS_Store`, `thumbs.db`, `*.swp`, `*.tmp`

**Validacion de Claves API:**
Verificar archivos modificados buscando patrones como:

```bash
OPENAI_API_KEY=sk-proj-xxxxx  # Real key detected!
AWS_SECRET_KEY=AKIA...         # Real key detected!
STRIPE_API_KEY=sk_live_...    # Real key detected!

# Placeholders aceptables:
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**Verificar:**

- `.gitignore` configurado correctamente
- Sin conflictos de merge
- Branch correcto (advertir si es main/master)
- Claves API son solo placeholders

### 3. Solicitar Confirmacion

Presentar resumen:

```text
Changes Summary:
- X archivos modificados, Y agregados, Z eliminados
- Total: +AAA inserciones, -BBB eliminaciones

Safety: No secrets | No large files | [advertencias]
Branch: [nombre] -> origin/[nombre]

Voy a: git add . -> commit -> push

Escribi 'yes' para proceder o 'no' para cancelar.
```

**ESPERAR un "yes" explicito antes de proceder.**

### 4. Ejecutar (Despues de Confirmacion)

Ejecutar secuencialmente:

```bash
git add .
git status  # Verificar staging
```

### 5. Generar Mensaje de Commit

Analizar cambios y crear conventional commit:

**Formato:**

```text
[tipo]: Resumen breve (max 72 caracteres)

- Cambio clave 1
- Cambio clave 2
- Cambio clave 3
```

**Tipos:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `build`, `ci`

**Ejemplo:**

```text
docs: Update concept README files with comprehensive documentation

- Add architecture diagrams and tables
- Include practical examples
- Expand best practices sections
```

### 6. Commit y Push

```bash
git commit -m "$(cat <<'EOF'
[Mensaje de commit generado]
EOF
)"
git push  # Si falla: git pull --rebase && git push
git log -1 --oneline --decorate  # Verificar
```

### 7. Confirmar Exito

```text
Successfully pushed to remote!

Commit: [hash] [mensaje]
Branch: [branch] -> origin/[branch]
Archivos cambiados: X (+inserciones, -eliminaciones)
```

## Manejo de Errores

- **git add falla**: Verificar permisos, archivos bloqueados, verificar que el repo esta inicializado
- **git commit falla**: Corregir pre-commit hooks, verificar git config (user.name/email)
- **git push falla**:
  - Non-fast-forward: `git pull --rebase && git push`
  - Sin branch remoto: `git push -u origin [branch]`
  - Branch protegido: Usar workflow de PR en su lugar

## Cuando Usar

**Bueno:**

- Actualizaciones de documentacion multi-archivo
- Feature con tests y docs
- Correcciones de bugs a traves de archivos
- Formateo/refactorizacion de todo el proyecto
- Cambios de configuracion

**Evitar:**

- No estas seguro de que se esta commiteando
- Contiene secretos/datos sensibles
- Branches protegidos sin review
- Conflictos de merge presentes
- Queres historial de commits granular
- Pre-commit hooks fallando

## Alternativas

Si el usuario quiere control, sugerir:

1. **Staging selectivo**: Revisar/agregar archivos especificos
2. **Staging interactivo**: `git add -p` para seleccion por parches
3. **Workflow de PR**: Crear branch -> push -> PR (usar comando `/pr`)

**Recordar**: Siempre revisar cambios antes de pushear. Ante la duda, usar comandos git individuales para mayor control.

---

**Ultima Actualizacion**: Abril 2026
