import React, {useEffect, useState} from 'react'

function Transaction({transaction}){
    const {input, output} = transaction;
    const recipient = Object.keys(output);

    if(input.address == "*--official-mining-reward--*"){
        input.address = `🎖️${input.address}🎖️`
    }

    return (
        <div className="Transaction">
            <div>From: {input.address}</div>
            {
                recipient.map(recipient => (
                    <div>
                        To : {recipient} | Sent : {output[recipient]}
                    </div>
                ))
            }
        </div>
    )
}

export default Transaction;