import React from 'react'
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Heading from '../Heading/Heading';
import Smallhead from '../Smallhead/Smallhead';
const Navigation = (Navigationbar) => {
  return (
    <div className=''>Navigation</div>
  )
}
export default function Navigationbar(){
    return(
        <Box >
            <AppBar position="static" >
                <Toolbar sx={{flexGrow:1, backgroundColor: "#2A4704"}}>
                    
                        
                        <Typography variant="h6" component="div" >
                            <Heading className="small-heading"/>
                            <Smallhead className="s-heading"/>
                        </Typography>
                        {/* <Button color="inherit">HOME</Button> */}
                    
                </Toolbar>
            </AppBar>
        </Box>
    );
}