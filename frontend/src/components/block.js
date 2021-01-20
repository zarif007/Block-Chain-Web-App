import React, {useState, useEffect} from 'react'
import {Button} from 'react-bootstrap'
import {MILLISECONDS_PY} from '../config'
import Transaction from './transaction'

function ToggleTransactionDisplay({ block }){
    const [displayTransaction, setDisplayTransaction] = useState(false);
    const {data} = block

    const toggleDisplayTransaction = () => {
        setDisplayTransaction(!displayTransaction);
    }


    if (displayTransaction){
        return (
            <div>{
                data.map(transansaction => (
                    <div>
                        <hr/>
                        <Transaction transaction={transansaction} />
                    </div>
                ))
            }
            <br/>
            <Button onClick={toggleDisplayTransaction}>Show less</Button>
            </div>
        )
    }

    return (
        <div>
            <br />
            <Button className="cstm-button" onClick={toggleDisplayTransaction}>Show more</Button>
        </div>
    )
}

function Block({ block }){
    const {timestamp, hash, data, last_hash} = block;
    const hashDisplay = hash;
    const timestampDisplay = new Date(timestamp / MILLISECONDS_PY).toLocaleString();
    const lasthash = last_hash;

    return(
        <div className="Block">
            <div>Previous Hash : {last_hash}</div>
            <div>Hash : {hashDisplay}</div>
            <div>TimeStamp : {timestampDisplay}</div>
            
            <ToggleTransactionDisplay block={block}/>
        </div>
    )
}

export default Block;