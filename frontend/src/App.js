import React, {useState} from 'react';
import axios from 'axios';

function App(){
  const [home, setHome] = useState('Hanshin');
  const [away, setAway] = useState('Yomiuri');
  const [result, setResult] = useState(null);

  const call = async () => {
    try{
      const resp = await axios.get('http://localhost:8000/predict', {
        params: {home_team: home, away_team: away}
      });
      setResult(resp.data);
    }catch(e){
      setResult({error:e.message});
    }
  };

  return (
    <div style={{padding:20,fontFamily:'sans-serif'}}>
      <h2>NPB Demo Predictor</h2>
      <div><label>Home: <input value={home} onChange={e=>setHome(e.target.value)} /></label></div>
      <div><label>Away: <input value={away} onChange={e=>setAway(e.target.value)} /></label></div>
      <button onClick={call} style={{marginTop:10}}>Predict</button>
      <pre style={{background:'#f6f6f6',padding:10,marginTop:10}}>{result?JSON.stringify(result,null,2):'No result yet'}</pre>
    </div>
  );
}

export default App;
