import React from 'react';
import ReactDOM from 'react-dom';
import {Router, Switch, Route} from 'react-router-dom';
import history from './history'
import './index.css';
import App from './components/App'
import Blockchain from './components/blockchain';
import ConductTransaction from './components/ConductTransactions'
import TransactionPool from './components/transaction_pool';

ReactDOM.render(
    <Router history={history}>
        <Switch>
            <Route path='/' exact component={App}/>
            <Route path='/blockchain' component={Blockchain}/>
            <Route path='/conduct-transaction' component={ConductTransaction}/>
            <Route path='/transaction-pool' component={TransactionPool}/>
        </Switch>
    </Router>
    ,document.getElementById('root')
);