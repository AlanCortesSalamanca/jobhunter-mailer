# 🚀 JobHunter Mailer

Automatiza el envío de correos personalizados a múltiples empresas usando un archivo Excel. Incluye logs en tiempo real, adjuntos (CV) y sistema anti-spam con delays inteligentes.

## ✨ Features

* 📧 Envío masivo de correos personalizados
* 🏢 Uso de `{empresa}` para personalización automática
* 📎 Adjuntar CV automáticamente
* 📊 Logs en tiempo real (SSE)
* ⏱️ Delay inteligente anti-spam
* 📂 Carga de archivos desde el frontend
* ⚡ Backend con FastAPI
* 🎨 Frontend con React + Vite

## 🛠️ Tech Stack

**Frontend**

* React
* Vite

**Backend**

* FastAPI
* Python
* SMTP (Gmail)

## 📂 Estructura del proyecto

```
jobhunter-mailer/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── services/
│   │   │   ├── email_sender.py
│   │   │   ├── file_parser.py
│   │   │   └── logger.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│
└── README.md
```

## ⚙️ Instalación

### 1. Clonar repo

```bash
git clone https://github.com/AlanCortesSalamanca/jobhunter-mailer.git
cd jobhunter-mailer
```


### 2. Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

uvicorn app.main:app --reload
```

Servidor en:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)


### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

App en:
👉 [http://localhost:5173](http://localhost:5173)


## 📄 Formato del Excel

Tu archivo debe tener columnas como:

| empresa | correo                                        |
| ------- | --------------------------------------------- |
| Google  | [jobs@google.com](mailto:jobs@google.com)     |
| Amazon  | [hiring@amazon.com](mailto:hiring@amazon.com) |


## 🧠 Uso

1. Ingresa tu correo Gmail
2. Usa una App Password (no tu contraseña normal)
3. Escribe el asunto
4. Escribe el mensaje usando `{empresa}`
5. Sube tu Excel
6. Sube tu CV
7. Haz clic en **Enviar**


## 📊 Logs en tiempo real

La app muestra:

* 📤 Correos enviados
* ✅ Éxitos
* ❌ Errores
* 📊 Progreso


## ⚠️ Notas importantes

* Usa App Password de Gmail
* No envíes demasiados correos muy rápido
* Respeta límites de Gmail (~100-150/día recomendados)


## 🚀 Roadmap

* [ ] Barra de progreso visual
* [ ] Historial de envíos
* [ ] Deploy en la nube
* [ ] UI mejorada


## 📸 Screenshots

<img width="318" height="46" alt="image" src="https://github.com/user-attachments/assets/29d75f7a-08e5-4d2c-a333-de849024fa29" />



## 🤝 Contribuciones

Pull requests bienvenidos 🚀


## 🧑‍💻 Autor

Desarrollado por Alan Cortes Salamanca

## ⭐ Si te gusta

Dale una estrella al repo ⭐

