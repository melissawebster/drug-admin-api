// Layout Imports
import 'bootstrap/dist/css/bootstrap.min.css'
import '../search-bar/SearchBar.css'

import React, { useState } from 'react';

interface CreateDrugFormProps {
  onSubmit: (formData: any) => void;
}

const CreateForm: React.FC<CreateDrugFormProps> = ({ onSubmit }) => {
  const [name, setName] = useState('');
  const [price, setPrice] = useState('');
  const [inStock, setInStock] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const formData = {
      name,
      price: parseFloat(price),
      stock: inStock
    };
    onSubmit(formData);
  };

  return (
    <form className="mt-3 p-3 form" onSubmit={handleSubmit}>
      <div className="my-3">
        <label>Name:</label>
        <input
          className="mx-2"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </div>
      <div className="my-3">
        <label>Price:</label>
        <input
          className="mx-2"
          type="text"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />
      </div>
      <div className="my-3">
        <label>In Stock:</label>
        <input
          className="mx-2"
          type="checkbox"
          checked={inStock}
          onChange={(e) => setInStock(e.target.checked)}
        />
      </div>
      <button className="form-button" 
              type="submit">Submit</button>
    </form>
  );
};

export default CreateForm;
