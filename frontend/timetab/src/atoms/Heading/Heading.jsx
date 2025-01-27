import React from 'react'
import "./Heading.css"
const Heading = (props) => {
  console.log(props.className)
  return (
    <div className={props.className}>TimeTAB</div>
   
  )
}
export default Heading