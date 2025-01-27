import { useState } from 'react'
import './App.css'
import Button from './atoms/Button/Button';
import Heading from './atoms/Heading/Heading';
import Dropdown from './atoms/dropdown/Dropdown';


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      
      <h1>TimeTAB</h1>
      
      <div className="App">
          <Button />
        </div>
      <div className='bar'>
        <Dropdown/>
        <Button/>
        <Heading/>
              </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
