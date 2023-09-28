import React from 'react';
import edit from '../../assets/edit.png';
import remove from '../../assets/remove.png';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Table.css'

interface TableProps {
    data: any[]; 
  }

  const Table: React.FC<TableProps> = ({ data }) => {
    return (
        <>
          <div className="container-fluid mt-3">
            <div className="row">
                <div className="col-8 mx-auto">
                    <table className="table-content container-fluid">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Price</th>
                                <th>In Stock</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            {data.map((item, index) => (
                                <tr key={index}>
                                    <td>{item.name}</td>
                                    <td>R$&nbsp;{item.price.toFixed(2)}</td>
                                    <td>{item.stock ? 'Yes' : 'No'}</td>
                                    <td>
                                        <img src={edit} alt="Edit" className="icon-table" />
                                        <img src={remove} alt="Remove" className="icon-table" />
                                    </td>
                                </tr>
                            ))}



                            {/* <tr>
                                <td>Vitex</td>
                                <td>R$33,50</td>
                                <td>Yes</td>
                                <td>
                                    <img src={edit} alt="Edit" className="icon-table" />
                                    <img src={remove} alt="Remove" className="icon-table" />
                                </td>
                            </tr> */}
                        </tbody>
                    </table>
                </div>
            </div>
          </div>
        </>
      )
}

export default Table