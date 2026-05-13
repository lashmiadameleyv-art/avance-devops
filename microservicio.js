
exports.handler = async (event) => {
    const mensajes = [
        "todo fluye bien",
        "tu transacción fue procesada exitosamente.",
        "el sistema está estable y seguro.",
        "bienvenido a soluciones tecnológicas del futuro."
    ];
    
    // elegimos un mensaje al azar
    const mensajeElegido = mensajes[Math.floor(Math.random() * mensajes.length)];
    
    const response = {
        statusCode: 200,
        body: JSON.stringify({
            estado: "exito",
            mensaje: mensajeElegido
        }),
    };
    return response;
};
