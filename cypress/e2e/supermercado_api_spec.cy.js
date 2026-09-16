describe('Pruebas de Integración de API - Supermercado ProductoPerecedero', () => {
  const baseUrl = 'http://127.0.0.1:8000/api/v1';
  let authToken = '';
  let productoId = null;

  before(() => {
    cy.request({
      method: 'POST',
      url: `${baseUrl}/auth/`,
      body: {
        username: 'Diego',
        password: 'Diego12345'
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('token');
      authToken = response.body.token;
    });
  });

  it('1. POST - Crear un nuevo ProductoPerecedero con Token', () => {
    cy.request({
      method: 'POST',
      url: `${baseUrl}/productos/`,
      headers: {
        Authorization: `Token ${authToken}`
      },
      body: {
        nombre: 'Queso Alpina Tajado 250g',
        sku: 'QUESO-ALP-250',
        precio_regular: 12000.00,
        dias_vencimiento: 4
      }
    }).then((response) => {
      expect(response.status).to.eq(201);
      expect(response.body).to.have.property('id');
      expect(response.body.precio_oferta).to.eq('9600.00');
      productoId = response.body.id;
    });
  });

  it('2. GET - Consultar el producto perecedero creado por ID', () => {
    cy.request({
      method: 'GET',
      url: `${baseUrl}/productos/${productoId}/`
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.nombre).to.eq('Queso Alpina Tajado 250g');
      expect(response.body.sku).to.eq('QUESO-ALP-250');
    });
  });

  it('3. DELETE - Eliminar el producto perecedero y verificar 204 No Content', () => {
    cy.request({
      method: 'DELETE',
      url: `${baseUrl}/productos/${productoId}/`,
      headers: {
        Authorization: `Token ${authToken}`
      }
    }).then((response) => {
      expect(response.status).to.eq(204);
    });
  });
});
