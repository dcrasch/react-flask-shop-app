var flux = new Fluxxor.Flux(stores, actions);

window.flux = flux;

React.render(
	<FluxProduct flux={flux} productid="1" />,
  document.getElementById('flux-product')
);
