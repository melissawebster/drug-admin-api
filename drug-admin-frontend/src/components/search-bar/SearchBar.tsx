// Layout Imports
import 'bootstrap/dist/css/bootstrap.min.css'
import './SearchBar.css'

// Components Imports
import CreateForm from '../create-form/CreateForm'
import Table from '../table/Table'

// Others
import { useState } from 'react'
import axios from 'axios'


function SearchBar () {

  const [name, setName] = useState('')
  const [data, setData] = useState<any[]>([])
  const [showForm, setShowForm] = useState(false);

  const fetchDataByName = () => {
    axios.get(`http://127.0.0.1:8000/drugs/get_by_name/${name}`)
      .then(res => setData(res.data))
      .catch(err => console.log(err))
  }

  const fetchAllData = () => {
    axios.get('http://127.0.0.1:8000/drugs/')
      .then(res => setData(res.data))
      .catch(err => console.log(err))
  }

  const handleAddNew = () => {
    setShowForm(true);
  };

  const handleCloseForm = () => {
    setShowForm(false);
  };

  const handleFormSubmit = (formData: any) => {
    axios.post('http://127.0.0.1:8000/drugs/post', formData)
      .then(res => {
        setData([...data, res.data]);
        setShowForm(false);
      })
      .catch(err => console.log(err));
  };

  return (
    <>
      <div className="search-bar container-fluid mt-5">

        <div className="row">
          <div className="col-8 mx-auto d-flex">
            Search for a drug
          </div>
        </div>

        <div className="row pt-2">
          <div className="col-8 mx-auto d-flex">
            <input 
              type="text" 
              className="text-input" 
              maxLength={50} 
              placeholder=" Type here..." 
              value={name} 
              onChange={(e) => setName(e.target.value)}
            />
            <button className="button mx-3" onClick={fetchDataByName}>Go</button>
            <span>or</span>
            <button className="button mx-3" onClick={fetchAllData}>Get&nbsp;all</button>
          </div>
        </div>

        <div className="row">
          <div className="col-8 mx-auto d-flex">
            <button className="button mt-3" onClick={handleAddNew}>Add new</button>
          </div>
        </div>

        {showForm && (
          <div className="row">
            <div className="col-8 mx-auto">
              <CreateForm onSubmit={handleFormSubmit} />
              <button className="button mt-3 mx-3" onClick={handleCloseForm}>Close</button>
            </div>
          </div>
        )}

        <Table data={data} />
      </div>
    </>
  );
}

export default SearchBar
