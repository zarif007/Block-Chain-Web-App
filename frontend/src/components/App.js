import React, {useState, useEffect} from 'react'
import {Link} from 'react-router-dom'
import logo from '../assets/logo.png'
import {API_BASE_URL} from '../config'

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
      <br/>
      <div>Total Block count : {blockchainLength}</div>
      <br/>
      <div className="WalletInfo">
        <div>Address: {address}</div>
        <div>Balance: {balance} ZedCoin</div>
      </div>
      <br></br>
      <div className="DisplayLink">
        <Link to='/blockchain' className="link">Blockchain</Link> <br/>
        <Link to='/conduct-transaction' className="link">Conduct a Transaction</Link> <br/>
        <Link to='/transaction-pool' className="link">Transaction Pool</Link>
      </div>
    </div>
  );
}

export default App;
