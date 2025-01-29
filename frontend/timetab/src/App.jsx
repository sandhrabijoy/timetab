import React,{ useState ,useEffect} from 'react';
import './App.css';
import Button from './atoms/Button/Button';
import Heading from './atoms/Heading/Heading';
import Dropdown from './atoms/dropdown/Dropdown';
import Smallhead from './atoms/Smallhead/Smallhead';
import Navigation from './atoms/Navigation/Navigation';
import Image from './atoms/Image/image';
import BasicTable from './atoms/Table/Table';
import axios from 'axios';

function App() {
  const[classOptions,setClassOptions]=useState([]);

  async function getdata() {
    try {
      const result = await fetch(`http://127.0.0.1:8000/class`);
      
      if (!result.ok) {
        throw new Error("No output");
      }
      
      const data = await result.json(); 
      console.log(data); 
      // const datas = Array.isArray(data) ? data[0] : [];
      const newdata = data.data; 
      console.log(newdata); 
      setClassOptions(newdata)
  
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }
  useEffect(()=>{
    
    getdata()
    // axios
    //   .get("http://127.0.0.1:8000/class/")
    //   .then((response) => {
    //     console.log(response)
    //     console.log(response.data);
    //     setClassOptions(response.data);
    //     console.log(farmerOptions)
    //   })
    //   .catch((error) => {
    //     console.error("There was an error!", error);
    //   });
  }, []); 

// useEffect(()=>{
// console.log(classOptions);
// },[classOptions]);

const handleSubmit=(e)=>{
  e.preventDefaultt();
  console.log("ButtonClicked");

}

  return (
    <>
      <div className="App">
        <Navigation />
        <Image />
        {/* <Descr /> */}
        
        <Heading className="big-heading" />

        <Smallhead className="b-heading" />

        <div className='bar'>
          <Dropdown options={classOptions}/>
          <Button className="button-style" text="SUBMIT" onClick={handleOnclick}/>
        </div>

        <BasicTable />

      </div>
    </>
  );
}

export default App;
