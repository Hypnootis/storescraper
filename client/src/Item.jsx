/* eslint-disable react/prop-types */
function Item({ product }) {
  return (
    <li>
      <p>
        <strong>Product name:</strong> {product.product_name}
      </p>
      <p>Unit price: {product.unit_price}</p>
      <p>Comparison price: {product.comparison_price}</p>
    </li>
  );
}

export default Item;
