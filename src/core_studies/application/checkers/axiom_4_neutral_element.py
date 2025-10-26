from typing import TypeVar, Generic 
from core_studies.domain.entities.Element import AlgebraicElement
from core_studies.domain.entities.VectorSpace import VectorSpace
from core_studies.domain.errors.exceptions import AxiomFailedError
from ..ports.axiom_checker import IAxiomCheckerPort

ET = TypeVar('ET', bound=AlgebraicElement)
NUM_SAMPLES = 3 


class CheckNeutralElement(Generic[ET], IAxiomCheckerPort[ET]):
    """
    Implementa a verificação para o Axioma 4:
    Existência de um Elemento Neutro (u + 0 = u).
    """

    @property
    def axiom_name(self) -> str:
        return "A4: Existência de Elemento Neutro"

    def check(self, space: VectorSpace[ET]) -> None:
        """
        Verifica se o elemento neutro (zero) fornecido pelo
        provedor do espaço realmente satisfaz u + 0 = u e 0 + u = u.
        """
        
        try:
            zero = space.zero_element_provider.get()
        except Exception as e:
            raise AxiomFailedError(f"Falha ao obter o elemento neutro: {e}")

        if not space.validator.validate(zero):
            raise AxiomFailedError(
                f"O elemento neutro fornecido '{zero}' "
                f"não pertence ao conjunto (validador falhou)."
            )

        try:
            samples = space.element_provider.get_elements(NUM_SAMPLES)
        except Exception as e:
            raise AxiomFailedError(f"Falha ao obter elementos de amostra: {e}")

        for u in samples:
            try:
                u_plus_zero = space.addition.execute(u, zero)
            except Exception as e:
                raise AxiomFailedError(
                    f"A operação falhou ao calcular {u} + {zero}. Erro: {e}"
                )
            
            if u_plus_zero != u:
                raise AxiomFailedError(
                    f"Falha na regra u + 0 = u. "
                    f"'{u} + {zero}' resultou em '{u_plus_zero}', mas deveria ser '{u}'."
                )

            try:
                zero_plus_u = space.addition.execute(zero, u)
            except Exception as e:
                raise AxiomFailedError(
                    f"A operação falhou ao calcular {zero} + {u}. Erro: {e}"
                )
            
            if zero_plus_u != u:
                raise AxiomFailedError(
                    f"Falha na regra 0 + u = u. "
                    f"'{zero} + {u}' resultou em '{zero_plus_u}', mas deveria ser '{u}'."
                )
        
        return None