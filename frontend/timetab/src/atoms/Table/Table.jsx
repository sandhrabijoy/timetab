import * as React from 'react';
import Table from '@mui/material/Table';
import { TableBody,TableContainer,TableHead,TableRow,Paper,TableCell } from '@mui/material';

function createData(id,Name,active){
    return {id,Name,active};
}

const rows=[
    createData(1,'ABC','Active'),
    createData(2,'PQR','Active'),
    createData(3,'XYZ','Non-Active')
]

export default function BasicTable(){
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
                            ACTIVE&nbsp;
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
              <TableCell align="right">{row.active}</TableCell>
            
            </TableRow>
          ))}
        </TableBody>
            </Table>
        </TableContainer>
    )
}