import { useState } from 'react'
import './EditModal.css'
import axios from 'axios'

interface EditModalProps {
    itemId: number
    onClose: () => void
    initialData: {
        name: string
        price: number
        stock: boolean
    }
}

const EditModal: React.FC<EditModalProps> = ({ itemId, onClose, initialData }) => {
    const [formData, setFormData] = useState((initialData))

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target
        setFormData({
            ...formData,
            [name]: name === 'stock' ? e.target.checked : value
        })
    }

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault()
        console.log(formData)
        console.log(itemId)
        axios.patch(`http://127.0.0.1:8000/drugs/update/${itemId}`, formData)
            .then(response => {
                console.log(response.data)
                onClose()
            })
            .catch(err => console.error(err))
    }

    return (
        <div className="modal-background">
            <div className="modal-box">
                <div className="modal-content">
                    <h5>Edit drug</h5>
                    <form onSubmit={handleSubmit}>
                        <div className="form-group my-2">
                            <label htmlFor="name">Name&nbsp;</label>
                            <input
                                type="text"
                                id="name"
                                name="name"
                                value={formData.name}
                                onChange={handleInputChange}
                            />
                        </div>
                        <div className="form-group my-2">
                            <label htmlFor="price">Price&nbsp;</label>
                            <input
                                type="number"
                                id="price"
                                name="price"
                                value={formData.price}
                                onChange={handleInputChange}
                            />
                        </div>
                        <div className="form-group my-2">
                            <label htmlFor="stock">In Stock&nbsp;</label>
                            <input
                                type="checkbox"
                                id="stock"
                                name="stock"
                                checked={formData.stock}
                                onChange={handleInputChange}
                            />
                        </div>
                        <div className="button-group my-3">
                            <button type="submit">Save</button>
                            <button type="button" onClick={onClose}>Cancel</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default EditModal
