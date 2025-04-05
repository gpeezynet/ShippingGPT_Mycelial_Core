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
    <div className="min-h-screen bg-gray-900 text-white p-6 space-y-8">
      <h1 className="text-4xl font-bold mb-6">📦 ShippingGPT Command Deck</h1>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Entropy Event Logger */}
        <div className="bg-gray-800 p-4 rounded-xl shadow col-span-1">
          <h2 className="text-2xl font-semibold mb-4">📝 Log Entropy Event</h2>
          <form onSubmit={handleSubmit} className="space-y-3">
            <input name="event_type" placeholder="Event Type" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600" />
            <input name="location" placeholder="Location" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600" />
            <input name="operator_id" placeholder="Operator ID" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600" />
            <select name="resolution_status" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600">
              <option value="">Resolution Status</option>
              <option value="open">open</option>
              <option value="resolved">resolved</option>
              <option value="escalated">escalated</option>
            </select>
            <input name="root_cause_tag" placeholder="Root Cause Tag" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600" />
            <textarea name="notes" placeholder="Notes" onChange={handleChange} className="w-full p-2 rounded bg-gray-700 border border-gray-600" rows={3} />
            <button className="w-full bg-green-600 hover:bg-green-700 py-2 rounded-lg font-semibold">Submit Event</button>
          </form>
        </div>

        {/* System Status Overview */}
        <div className="bg-gray-800 p-4 rounded-xl shadow col-span-1">
          <h2 className="text-2xl font-semibold mb-4">🧠 System Status</h2>
          <ul className="list-disc pl-5 space-y-2 text-sm">
            <li>ShippingGPT: Active ✅</li>
            <li>FeedbackGPT: Monitoring escalation 📈</li>
            <li>packing_station_v2.md: ✅ Deployed</li>
            <li>label_pipeline_v2.md: ⚠️ Pending Deployment</li>
            <li>Entropy Monitor: 🟢 Watching last 7 days</li>
          </ul>
        </div>

        {/* Recent Events Table */}
        <div className="bg-gray-800 p-4 rounded-xl shadow col-span-1 lg:col-span-1 overflow-auto">
          <h2 className="text-2xl font-semibold mb-4">📊 Recent Entropy Events</h2>
          <table className="w-full text-sm border-collapse">
            <thead>
              <tr className="text-left border-b border-gray-700">
                <th className="py-1">Date</th>
                <th className="py-1">Type</th>
                <th className="py-1">Loc</th>
                <th className="py-1">Op</th>
                <th className="py-1">Status</th>
                <th className="py-1">Root</th>
              </tr>
            </thead>
            <tbody>
              {logs.map((log, index) => (
                <tr key={index} className="border-b border-gray-700">
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
    </div>
  );
}
