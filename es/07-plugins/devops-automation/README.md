<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Plugin de automatizacion DevOps

Automatizacion DevOps completa para deploy, monitoreo y respuesta a incidentes.

## Funcionalidades

✅ Deployments automatizados
✅ Procedimientos de rollback
✅ Monitoreo de salud del sistema
✅ Workflows de respuesta a incidentes
✅ Integracion con Kubernetes

## Instalacion

```bash
/plugin install devops-automation
```

## Que incluye

### Slash Commands
- `/deploy` - Hacer deploy a produccion o staging
- `/rollback` - Hacer rollback a la version anterior
- `/status` - Verificar la salud del sistema
- `/incident` - Gestionar incidentes en produccion

### Subagentes
- `deployment-specialist` - Operaciones de deployment
- `incident-commander` - Coordinacion de incidentes
- `alert-analyzer` - Analisis de salud del sistema

### Servidores MCP
- Integracion con Kubernetes

### Scripts
- `deploy.sh` - Automatizacion de deployment
- `rollback.sh` - Automatizacion de rollback
- `health-check.sh` - Utilidades de verificacion de salud

### Hooks
- `pre-deploy.js` - Validacion previa al deployment
- `post-deploy.js` - Tareas posteriores al deployment

## Uso

### Deploy a staging
```
/deploy staging
```

### Deploy a produccion
```
/deploy production
```

### Rollback
```
/rollback production
```

### Verificar estado
```
/status
```

### Gestionar incidente
```
/incident
```

## Requisitos

- Claude Code 1.0+
- Kubernetes CLI (kubectl)
- Acceso al cluster configurado

## Configuracion

Configurar tu Kubernetes config:
```bash
export KUBECONFIG=~/.kube/config
```

## Ejemplo de workflow

```
User: /deploy production

Claude:
1. Runs pre-deploy hook (validates kubectl, cluster connection)
2. Delegates to deployment-specialist subagent
3. Runs deploy.sh script
4. Monitors deployment progress via Kubernetes MCP
5. Runs post-deploy hook (waits for pods, smoke tests)
6. Provides deployment summary

Result:
✅ Deployment complete
📦 Version: v2.1.0
🚀 Pods: 3/3 ready
⏱️  Time: 2m 34s
```
