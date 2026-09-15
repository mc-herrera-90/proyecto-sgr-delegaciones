document.addEventListener("DOMContentLoaded", () => {

    const formulario = document.getElementById("login");
    const formularioAdmin = document.getElementById("login-form");

    const rutInput = document.getElementById("username");
    const rutInputAdmin = document.getElementById("id_username");

    function formatear(event) {
        let rut = event.target.value
            .replace(/[^0-9kK]/g, "")
            .toUpperCase();

        if (rut.length > 1) {
            const dv = rut.slice(-1);
            const cuerpo = rut.slice(0, -1);

            const formateado = cuerpo
                .replace(/\B(?=(\d{3})+(?!\d))/g, ".");

            rut = `${formateado}-${dv}`;
        }

        event.target.value = rut;    
    }

    rutInput?.addEventListener("input", (event) => formatear(event));
    rutInputAdmin?.addEventListener("input", (event) => formatear(event));

    // Validación y formato desde el cliente
    formulario?.addEventListener("submit", (event) => {
        const rutInput = event.target.username;
        rutInput.value = event.target.username.value.replace(/\./g, "");
    })

    formularioAdmin?.addEventListener("submit", (event) => {
        const rutInputAdmin = event.target.id_username;
        rutInputAdmin.value = event.target.id_username.value.replace(/\./g, "");
    })

})