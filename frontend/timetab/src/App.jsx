import { useState } from 'react';
import './App.css';
import Button from './atoms/Button/Button';
import Heading from './atoms/Heading/Heading';
import Dropdown from './atoms/dropdown/Dropdown';
import Smallhead from './atoms/Smallhead/Smallhead';
import Navigation from './atoms/Navigation/Navigation';
import Image from './atoms/Image/image';
import Descr from './atoms/Descr/Descr';
import BasicTable from './atoms/Table/Table';

function App() {
  // If you intend to use count
  const [count, setCount] = useState(0);

  return (
    <>
      <div className="App">
        <Navigation />
        <Image />
        <Descr />
        
        <Heading className="big-heading" />

        <Smallhead className="b-heading" />

        <div className='bar'>
          <Dropdown />
          <Button className="button-style" text="SUBMIT" />
        </div>

        <BasicTable />

      </div>
    </>
  );
}

export default App;
