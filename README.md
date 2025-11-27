# 🎮 Piedra, Papel o Tijera

Este proyecto es un juego sencillo de **Piedra, Papel o Tijera** desarrollado en Python, que se ejecuta desde consola e incluye **pruebas unitarias con Pytest**.  
Además, cuenta con un flujo de **CI/CD automatizado usando GitHub Actions**, el cual ejecuta pruebas con cada commit realizado en la rama `development` y realiza merge automático hacia la rama `qualityassurance` cuando estas pruebas pasan correctamente.

---

## 🚀 Características principales
- Juego interactivo en consola.
- Lógica modular separada en `game.py`.
- Pruebas unitarias con Pytest ubicadas en `/tests`.
- Pipeline CI/CD configurado con GitHub Actions.
- Automatización del merge hacia QA si las pruebas pasan.

---

## 📂 Estructura del proyecto

```
OSCARREYES1031155272/
│
├─ .github
│   └─ workflows
│       └─ CI-CD.yml
│
├─ tests
│   └─ test_game.py
│
├─ game.py
├─ main.py
├─ README.md
├─ requirements.txt
```

---

## ▶️ Cómo jugar

Ejecuta el siguiente comando en una terminal dentro del proyecto:

```bash
python main.py
```

El sistema solicitará tu elección y mostrará el resultado del enfrentamiento contra la computadora.

---

## 🧪 Ejecutar pruebas unitarias

Primero instala las dependencias:

```bash
pip install -r requirements.txt
```

Luego ejecuta las pruebas:

```bash
pytest -v
```

---

## 🔁 CI/CD con GitHub Actions
| Acción | Resultado |
|------|----------------|
| **Commit en development** | Se ejecutan pruebas automatizadas |
| **Si todas pasan** | Merge automático hacia qualityassurance |
| **Si tiene errores** | El pipeline falla y NO se hace merge |

Puedes ver la ejecución desde:
- GitHub → Actions

---

## 🛠 Tecnologías utilizadas

- Python 3.x
- Pytest
- GitHub Actions (CI/CD)
- Git & GitHub

---

## 👨‍💻 Autor

Oscar Danilo Reyes Briceño