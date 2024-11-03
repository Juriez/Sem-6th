import { useState } from 'react';
import './App.css';

function App() {
    const [output, setOutput] = useState(''); // State for API output

    // Function to hit the API
    const hitApi = async (id) => {
        try {
            const res = await fetch(`http://localhost:3000/api${id}`, { method: 'POST' });
            if (!res.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await res.json();

            // Clear output and show results based on response
            if (data.response === 'error') {
                setOutput(prev => `${prev}\nAPI ${id} Call Failed: ${data.callsInMinute} requests in the last minute. Allowed: ${data.allowedHits}. TTL: ${data.ttl}`);
            } else {
                setOutput(prev => `${prev}\nAPI ${id} Call Successful: ${data.response}. Calls in the last minute: ${data.callsInMinute}. TTL: ${data.ttl}`);
            }
        } catch (error) {
            console.error('Error fetching the API:', error);
            setOutput(prev => `${prev}\nError: ${error.message}`);
        }
    };

    return (
        <>
            <h1>Rate Limiter Implementation</h1>
            <h2>API Output:</h2>
            <pre>{output}</pre>
            <button onClick={() => hitApi(1)}>Hit API 1</button>
            <button onClick={() => hitApi(2)}>Hit API 2</button>
            <button onClick={() => hitApi(3)}>Hit API 3</button>
        </>
    );
}

export default App;
