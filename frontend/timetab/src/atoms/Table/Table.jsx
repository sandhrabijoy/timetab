import * as React from 'react';
import Table from '@mui/material/Table';
import { TableBody,TableContainer,TableHead,TableRow,Paper,TableCell } from '@mui/material';

function createData(id,name,teachername){
    return {id,name,teachername};
}

const rows=[
    createData(1,'ABC','Susan'),
    createData(2,'PQR','alexa'),
    createData(3,'XYZ','Mathew')
]

export default function BasicTable({rows}){
    return(
        <TableContainer component={Paper}>
            <Table sx={{minWidth:650}} aria-label='simple table'>
                <TableHead sx={{ backgroundColor: '#F4F4E1' }}>
                    <TableRow>
                        <TableCell>
                            ID
                        </TableCell>
                        <TableCell align='right'>
                           CLASS NAME
                        </TableCell>
                        <TableCell align='right'>
                            TEACHER NAME&nbsp;
                        </TableCell>
                    </TableRow>
                    
                </TableHead>
                <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } , backgroundColor: '#F4F4E1', }}
            >
              <TableCell component="th" scope="row">
                {row.id}
              </TableCell>
              <TableCell align="right">{row.name}</TableCell>
              <TableCell align="right">{row.teachername}</TableCell>
            
            </TableRow>
          ))}
        </TableBody>
            </Table>
        </TableContainer>
    )
}