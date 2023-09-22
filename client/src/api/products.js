import axios from "axios";

const URL = import.meta.env.VITE_API || "http://localhost:8000";
const endpoint = URL + "/api/products";

export const fetchProducts = () => axios.get(endpoint);

export const fetchProduct = (id) => axios.get(`${endpoint}/${id}`);

export const createProduct = (product) => axios.post(endpoint, product);

export const updateProduct = (id, product) =>
  axios.put(`${endpoint}/${id}`, product);

export const deleteProduct = (id) => axios.delete(`${endpoint}/${id}`);
