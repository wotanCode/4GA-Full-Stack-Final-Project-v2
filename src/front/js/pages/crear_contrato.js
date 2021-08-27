import React from "react";
import { Link, useParams } from "react-router-dom";

//Componentes importados
import { CrearcontratoComponent } from "../component/crear_contrato_component.js";
import { Crearordeninv } from "../component/Crearordeninv.js";

//react-bootstrap
import { Container, Row, Col, Form, Button } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

export const Crearcontrato = () => {
	return (
		<Container className="mb-3">
			<Form className="ml-5 border">
				<CrearcontratoComponent />
				<Crearordeninv />
				<Button className="my-3" variant="primary">
					Crear
				</Button>{" "}
			</Form>
		</Container>
	);
};
