import React,{ useState ,useEffect} from 'react';
import './App.css';
import Button from './atoms/Button/Button';
import Heading from './atoms/Heading/Heading';
import Dropdown from './atoms/dropdown/Dropdown';
import Smallhead from './atoms/Smallhead/Smallhead';
import Navigation from './atoms/Navigation/Navigation';
import Image from './atoms/Image/image';
import BasicTable from './atoms/Table/Table';


function App() {
  const[classOptions,setClassOptions]=useState([]);
  const[idStore,setIdStore]=useState(null);
  const [fetchedData, setFetchedData] = useState([]);

  // const handleSubmit=(e)=>{
  //   e.preventDefault();
  //   console.log("ButtonClicked");
  
  // }
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
  }, []); 

  async function handleOnclick() {
    try {
      const result = await fetch(`http://127.0.0.1:8000/class/${idStore}`);
      
      if (!result.ok) {
        throw new Error("Please Select a class first");
      }
      
      const data = await result.json(); 
      console.log("hi",data); 
      // const datas = Array.isArray(data) ? data[0] : [];
      const newdata = data.data; 
      console.log('dataaa',newdata); 
      setFetchedData(newdata)
      console.log('val',fetchedData);
  
    } catch (error) {
      console.error("Error fetching data:", error);
    }
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
          <Dropdown options={classOptions} setidStore={setIdStore} idStore={idStore}/>
          <Button className="button-style" text="SUBMIT" onClick={handleOnclick}/>
        </div>

        <BasicTable rows={fetchedData} />

      </div>
    </>
  );
}

export default App;
