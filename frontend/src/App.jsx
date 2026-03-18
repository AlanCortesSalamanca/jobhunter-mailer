import { useState, useEffect } from "react";

function App() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [subject, setSubject] = useState("");
  const [body, setBody] = useState("");
  const [excel, setExcel] = useState(null);
  const [cv, setCv] = useState(null);
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    const eventSource = new EventSource("http://127.0.0.1:8000/logs");

    eventSource.onmessage = (event) => {
      console.log("LOG:", event.data); // 👈 debug
      setLogs((prev) => [...prev, event.data]);
    };

    eventSource.onerror = (err) => {
      console.error("SSE error", err);
    };

    return () => eventSource.close();
  }, []);

  const handleSubmit = async () => {
    try {
      const formData = new FormData();

      formData.append("sender_email", email);
      formData.append("sender_password", password);
      formData.append("subject", subject);
      formData.append("body", body);
      formData.append("excel", excel);
      formData.append("cv", cv);

      console.log("Enviando request...");

      const res = await fetch("http://127.0.0.1:8000/send-emails", {
        method: "POST",
        body: formData
      });

      console.log("Respuesta recibida");

      const data = await res.json();

      console.log("DATA:", data);
      alert("Correos enviados");

    } catch (error) {
      console.error("ERROR:", error);
      alert("Error al enviar");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Job Hunter Mailer</h1>

      <input placeholder="Correo" onChange={(e) => setEmail(e.target.value)} />
      <br /><br />

      <input placeholder="App password" onChange={(e) => setPassword(e.target.value)} />
      <br /><br />

      <input placeholder="Asunto" onChange={(e) => setSubject(e.target.value)} />
      <br /><br />

      <textarea placeholder="Mensaje {empresa}" onChange={(e) => setBody(e.target.value)} />
      <br /><br />

      <br />Selecciona el Excel<br />
      <input type="file" onChange={(e) => setExcel(e.target.files[0])} />
      <br /><br />

      <br />Selecciona tu CV<br />
      <input type="file" onChange={(e) => setCv(e.target.files[0])} />
      <br /><br />

      <button onClick={handleSubmit}>Enviar</button>

      <h2>Logs</h2>

      <div style={{
        background: "#111",
        color: "#0f0",
        padding: "10px",
        height: "200px",
        overflow: "auto"
      }}>
        {logs.map((log, index) => (
          <div key={index}>{log}</div>
        ))}
      </div>
    </div>
  );
}

export default App;