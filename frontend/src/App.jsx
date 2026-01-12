import { useState } from "react";

const API = import.meta.env.VITE_BACKEND_URL;

export default function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [chart, setChart] = useState(null);

  async function upload() {
    const form = new FormData();
    form.append("file", file);
    await fetch(`${API}/upload`, { method: "POST", body: form });
  }

  async function ask() {
    const res = await fetch(`${API}/query`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });
    const data = await res.json();
    setAnswer(data.answer);
    setChart(data.chart || null);
  }

  return (
    <div style={{ padding: 40 }}>
      <h1>📊 Financial Chatbot</h1>

      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={upload}>Upload Data</button>

      <hr />

      <input
        style={{ width: "60%" }}
        placeholder="Ask a financial question..."
        value={question}
        onChange={e => setQuestion(e.target.value)}
      />
      <button onClick={ask}>Ask</button>

      <p>{answer}</p>
      {chart && <img src={`data:image/png;base64,${chart}`} />}
    </div>
  );
}
