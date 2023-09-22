import { useState, useEffect } from "react";
import {
  createProduct,
  fetchProduct,
  updateProduct,
  deleteProduct,
} from "../api/products";
import { useParams, useNavigate } from "react-router-dom";

function ProductForm() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [category, setCategory] = useState("");
  const [quantity, setQuantity] = useState("");
  const [price, setPrice] = useState("");

  const params = useParams();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      if (!params.id) {
        const res = await createProduct({
          title,
          description,
          category,
          quantity,
          price,
        });
        console.log(res);
      } else {
        const res = await updateProduct(params.id, {
          title,
          description,
          category,
          quantity,
          price,
        });
        console.log(res);
      }
      navigate("/");
    } catch (error) {
      console.error(error);
      if (error.response?.data) {
        alert(error.response.data.detail);
      }
    }

    e.target.reset();
  };

  useEffect(() => {
    if (params.id) {
      fetchProduct(params.id)
        .then((res) => {
          setTitle(res.data.title);
          setDescription(res.data.description);
          setCategory(res.data.category);
          setQuantity(res.data.quantity);
          setPrice(res.data.price);
        })
        .catch((error) => {
          console.error(error);
        });
    }
  }, []);

  return (
    <div className="flex items-center justify-center h-[calc(100vh-10rem)]">
      <div>
        <form className="bg-zinc-950 p-10" onSubmit={handleSubmit}>
          <h1 className="text-3xl font-bold my-4">Create Product</h1>
          <input
            type="text"
            placeholder="title"
            className="block p-2 py-2 px-3 mb-4 w-full text-black"
            onChange={(e) => setTitle(e.target.value)}
            value={title}
            autoFocus
          />
          <textarea
            placeholder="description"
            className="block p-2 py-2 px-3 mb-4 w-full text-black"
            onChange={(e) => setDescription(e.target.value)}
            value={description}
          ></textarea>
          <input
            type="text"
            placeholder="category"
            className="block p-2 py-2 px-3 mb-4 w-full text-black"
            onChange={(e) => setCategory(e.target.value)}
            value={category}
            autoFocus
          />
          <input
            type="number"
            placeholder="quantity"
            className="block p-2 py-2 px-3 mb-4 w-full text-black"
            onChange={(e) => setQuantity(e.target.value)}
            value={quantity}
            autoFocus
          />
          <input
            type="number"
            placeholder="price"
            className="block p-2 py-2 px-3 mb-4 w-full text-black"
            onChange={(e) => setPrice(e.target.value)}
            value={price}
            autoFocus
            step="0.01"
          />
          <button className="bg-white hover:bg-slate-800 hover:text-white text-slate-800 font-bold py-2 px-4 rounded">
            {params.id ? "Update" : "Create"}
          </button>
        </form>

        {params.id && (
          <button
            className="bg-red-500 hover:bg-red-400 text-white font-bold py-2 px-4 rounded mt-5"
            onClick={async () => {
              try {
                const res = await deleteProduct(params.id);
                console.log(res);
                navigate("/");
              } catch (error) {
                console.error(error);
              }
            }}
          >
            Delete
          </button>
        )}
      </div>
    </div>
  );
}

export default ProductForm;
