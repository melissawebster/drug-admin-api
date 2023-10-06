// Layout Imports
import 'bootstrap/dist/css/bootstrap.min.css'
import './Table.css'

// Static Imports
import edit from '../../assets/edit.png'
import remove from '../../assets/remove.png'

// Others
import axios from 'axios'
import { useState } from 'react'
import ConfirmModal from '../confirm-modal/ConfirmModal'


interface TableProps {
    data: any[]
}

const Table: React.FC<TableProps> = ({ data }) => {
    const [showDelModal, setShowDelModal] = useState(false)
    const [itemIdToDelete, setItemIdToDelete] = useState<number | null>(null)

    const openDelModal = (id: number) => {
        setItemIdToDelete(id);
        setShowDelModal(true);
    }

    const closeDelModal = () => {
        setItemIdToDelete(null);
        setShowDelModal(false);
    }

    const removeItem = (id: number) => {
        console.log(`Tentando remover o item com o ID ${id}`)
        axios.delete(`http://127.0.0.1:8000/drugs/delete/${id}`)
            .then(response => {
                console.log('Item removido com sucesso', response.data)
                closeDelModal()
                window.location.href = '/'
            })
            .catch(error => {
                console.error('Erro ao remover o item', error)
            });
    }

    return (
        <>
            {showDelModal && (
                <ConfirmModal
                    message = "Tem certeza que deseja excluir este item?"
                    onConfirm = {() => {
                        removeItem(itemIdToDelete!)
                    }}
                    onCancel={closeDelModal}
                />
            )}

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
                                {data.map((item) => (
                                    <tr key={item.id}>
                                        <td>{item.name}</td>
                                        <td>R$&nbsp;{item.price.toFixed(2)}</td>
                                        <td>{item.stock ? 'Yes' : 'No'}</td>
                                        <td>
                                            <img src={edit} 
                                                 alt="Edit"
                                                 title="Edit" 
                                                 className="icon-table" />
                                            <img 
                                                src={remove} 
                                                alt="Remove"
                                                title="Remove"  
                                                className="icon-table" 
                                                onClick={() => openDelModal(item.id)}
                                            />
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                            <tfoot>
                                <tr>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                    <td></td>
                                </tr>
                            </tfoot>
                        </table>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Table;
