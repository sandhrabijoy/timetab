import React from 'react'
import "./Button.css"
const Button=(props)=>{
    return(
        <div>
            <button className='button-style'>
                SUBMIT
            </button>
            <button className={props.className}>
                {props.text}
            </button>
        </div>
    )
} 
export default Button