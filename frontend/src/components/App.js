import React, {useState, useEffect} from 'react'
import logo from '../assets/logo.png'
import {API_BASE_URL} from '../config'

import Blockchain from './blockchain'

function App() {
  const [walletInfo, setWalletInfo] = useState({})
  const [blockchainLength, setBlockchainLength] = useState([]);

  useEffect(() => {
    fetch(`${API_BASE_URL}wallet/info`)
      .then(response => response.json())
      .then(json => setWalletInfo(json))
      
    fetch(`${API_BASE_URL}blockchain/length`)
      .then(response => response.json())
      .then(json => setBlockchainLength(json));
  }, []);

  const {address, balance} = walletInfo; 

  return (
    <div className="App">
      <img className="logo" src={logo} alt="logo"/>
      <h1>Welcome to ZedChain </h1>
      <div>Total Block count : {blockchainLength}</div>
      <br></br>
      <div className="WalletInfo">
        <div>Address: {address}</div>
        <div>Balance: {balance} ZedCoin</div>
      </div>
      <br/>
      <Blockchain />
    </div>
  );
}

export default App;
