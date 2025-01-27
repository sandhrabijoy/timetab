import React from 'react'
import "./Button.css"
const Button=(props)=>{
    return(
        <div>
            {/* <button className='button-style'>
                SUBMIT
            </button> */}
            {/* <button className={props.className}>
                {props.text}
            </button> */}
             <div>
      <button className={props.className}onClick={props.Onclick} >{props.text}</button>
    </div>
            
        </div>
    )
} 
export default Button