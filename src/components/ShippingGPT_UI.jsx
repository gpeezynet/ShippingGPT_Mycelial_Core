import React, { useState, useEffect } from "react";

export default function ShippingGPT_UI() {
  const [logs, setLogs] = useState([]);
  const [form, setForm] = useState({
    event_type: "",
    location: "",
    operator_id: "",
    resolution_status: "",
    root_cause_tag: "",
    notes: ""
  });

  useEffect(() => {
    fetch("http://localhost:5000/entropy/week")
      .then((res) => res.json())
      .then((data) => setLogs(data));
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("http://localhost:5000/entropy/log", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });
    if (res.ok) {
      alert("✅ Event submitted successfully");
      window.location.reload();
    }
  };

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">📦 ShippingGPT Dashboard</h1>

      {/* Entropy Event Logger */}
      <div className="bg-white p-4 rounded-xl shadow">
        <h2 className="text-xl font-semibold mb-4">📝 Log Entropy Event</h2>
        <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <input name="event_type" placeholder="Event Type" onChange={handleChange} className="input" />
          <input name="location" placeholder="Location" onChange={handleChange} className="input" />
          <input name="operator_id" placeholder="Operator ID" onChange={handleChange} className="input" />
          <select name="resolution_status" onChange={handleChange} className="input">
            <option value="">Resolution Status</option>
            <option value="open">open</option>
            <option value="resolved">resolved</option>
            <option value="escalated">escalated</option>
          </select>
          <input name="root_cause_tag" placeholder="Root Cause Tag" onChange={handleChange} className="input" />
          <textarea name="notes" placeholder="Notes" onChange={handleChange} className="input col-span-2" rows={3} />
          <button className="col-span-2 bg-black text-white py-2 rounded-lg">Submit Event</button>
        </form>
      </div>

      {/* Recent Events Table */}
      <div className="bg-white p-4 rounded-xl shadow">
        <h2 className="text-xl font-semibold mb-4">📊 Recent Entropy Events</h2>
        <table className="w-full text-sm">
          <thead>
            <tr>
              <th>Date</th>
              <th>Type</th>
              <th>Location</th>
              <th>Operator</th>
              <th>Status</th>
              <th>Root Cause</th>
            </tr>
          </thead>
          <tbody>
            {logs.map((log, index) => (
              <tr key={index}>
                <td>{new Date(log.timestamp).toLocaleString()}</td>
                <td>{log.event_type}</td>
                <td>{log.location}</td>
                <td>{log.operator_id}</td>
                <td>{log.resolution_status}</td>
                <td>{log.root_cause_tag}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
