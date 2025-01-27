import { useState } from 'react'
import './App.css'
import Button from './atoms/Button/Button';
import Heading from './atoms/Heading/Heading';
import Dropdown from './atoms/dropdown/Dropdown';
import Smallhead from './atoms/Smallhead/Smallhead';
import Navigation from './atoms/Navigation/Navigation';
import Image from './atoms/Image/image';
import Descr from './atoms/Descr/Descr';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      
      <h1>TimeTAB</h1>
      
     
      <div className='bar'>
        <Dropdown/>
        <Button/>
        
        <Heading className="big-heading"></Heading>
        <Heading className="small-heading"></Heading>
        <Smallhead className="b-heading"></Smallhead>
        <Smallhead className="s-heading"></Smallhead>
        <Descr/>
        <Image/>
        <Navigation/>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
