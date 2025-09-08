import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import CBKCDialog from '../../../components/CBKCDialog';
import { formatDateTimeWithTimezone } from '../../../util/formatDates';

const TryoutFIghtersCard = ({ fighter }) => {
	return (
		<Card
			sx={{
				height: '100%',
				display: 'flex',
				flexDirection: 'column',
				justifyContent: 'space-between',
				maxWidth: '100%',
				paddingBottom: 1,
			}}>
			<CardMedia
				sx={{ height: 200 }}
				image={`${import.meta.env.VITE_API_URL}${fighter.image}`}
				title={fighter.first_name}
			/>
			<CardContent sx={{ flexGrow: 1 }}>
				<Typography gutterBottom variant='h5' component='div' noWrap>
					{fighter.first_name} {fighter.last_name}
				</Typography>
				<Typography variant='body2' sx={{ color: 'text.secondary', wordWrap: 'break-word' }}>
					Weight: {fighter.weight_class}
				</Typography>
				<Typography variant='body2' sx={{ color: 'text.secondary', wordWrap: 'break-word' }}>
					{fighter.phone}
				</Typography>
				<Typography variant='body2' sx={{ color: 'text.secondary', wordWrap: 'break-word' }}>
					{fighter.email}
				</Typography>
			</CardContent>
			<CardActions>
				<CBKCDialog
					buttonName={'View Fighter'}
					popUpTitle={`${fighter.first_name} ${fighter.last_name}`}
					noSubmitBtn
					popupText={''}
					dialogSize={'md'}>
					{() => (
						<>
							<Typography variant='body2'>Weight: {fighter.weight_class}</Typography>
							<Typography variant='body2'>Phone Number: {fighter.phone}</Typography>
							<Typography variant='body2'>Email: {fighter.email}</Typography>
							<Typography variant='body2'>Experience (yrs): {fighter.experience_years}</Typography>
							<Typography variant='body2'>
								Date Registered: {formatDateTimeWithTimezone(fighter.date_registered)}
							</Typography>
						</>
					)}
				</CBKCDialog>
			</CardActions>
		</Card>
	);
};

export default TryoutFIghtersCard;
