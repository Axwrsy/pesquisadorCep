import React, { useState } from 'react';

const Box = () => {
  const [cep, setCep] = useState("");
  const [result, setResult] = useState(null);

  const handleClick = async () => {
    try {
      const url = `https://viacep.com.br/ws/${cep}/json/`;
      const response = await fetch(url);
      const data = await response.json();

      if (data.erro) {
        alert("cep não encontrado, verifique se digitou corretamente ");
        setResult(null);
      } else {
        setResult(data);
      }
    } catch (error) {
      console.error("erro ao buscar CEP:", error);
    }
  };

  return (
    <div className="container">
      <div className="nav">
        <h1>Consultar CEP</h1>

        <input className="input-field" type="text" placeholder="digite o cep: " maxLength={8} value={cep} onChange={(e) => setCep(e.target.value)}/>

        <button type="button" onClick={handleClick}>
          Consultar
        </button>
      </div>

      {/* mostra os dados se existir */}
      {result && (
        <div className="resultado">
          <p><strong>Logradouro:</strong> {result.logradouro}</p>
          <p><strong>Bairro:</strong> {result.bairro}</p>
          <p><strong>Cidade:</strong> {result.localidade}</p>
          <p><strong>Estado:</strong> {result.uf}</p>
        </div>
      )}
    </div>
  );
};

export default Box;
