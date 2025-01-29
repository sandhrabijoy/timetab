
import React from 'react'
import"./Dropdown.css"
import Select from '@mui/material/Select';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';

const Dropdown = ({options}) => {
  console.log('from dropdown',options)
  return (
    <div>
      <Box sx={{borderBottom:0}}>
     
      <FormControl fullWidth>
      <InputLabel id="demo-simple-select-label">Select Class</InputLabel>
        <Select 
        sx={{fontWeight:"regular",border:"0",height:"53px",width:"563px",backgroundColor:'#BACD9B',fontFamily: 'Inter',fontSize:30, '&:before': {borderBottom: 'none'} }}
        labelId="demo-simple-select-label"
        id="demo-simple-select"
        
        label="Select Farmer Company"
        >
         {options.length > 0 ? (
          options.map((option) => (
            <MenuItem key={option.id} value={option.id}>
              {option.name}
            </MenuItem>
          ))
        ) : (
          <MenuItem disabled>No options available</MenuItem>
        )} 
            
        </Select>
        </FormControl>
        </Box>
    </div>
  )
}
export default Dropdown